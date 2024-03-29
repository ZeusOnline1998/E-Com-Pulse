from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CustomUser, Product, Platform, ProductDetails, KeywordSearchResult, ProductArea, KeywordTbl, ProjectIdentifier
from datetime import timedelta, datetime
from django.db.models import Max, F
from .serializers import KeywordListSerializer, KeywordFilterDataSerializer, PlatformListSerializer, BrandListSerializer, KeywordSearchResultSerializer, ProductListSerializer
# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from rest_framework import status
import pandas as pd
from io import BytesIO
from django.http import HttpResponse

# Create your views here.
time_range = {
    1: timedelta(days=1),
    2: timedelta(days=7),
    3: timedelta(days=14),
}

keyword_time_range = {
    "1": timedelta(days=0),
    "2": timedelta(days=7)
}

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),  # type: ignore
    }

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email=email, password=password)
        print(user)
        if user:
            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            return Response({
                'access': str(access),
                'refresh': str(refresh),
            })
        # else:
    return Response({"error": "Invalid Credentials"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_access_token(request):
    user = request.user
    # Check if the access token is expired
    access_token = AccessToken.for_user(user)
    expiration_timestamp = access_token.payload.get("exp", None)

    if expiration_timestamp:
        current_timestamp = int(datetime.timestamp(datetime.now()))
        if current_timestamp > int(expiration_timestamp):
            refresh_token = RefreshToken.for_user(user)
            if refresh_token.is_expired:
                # Both access and refresh tokens are expired; generate new tokens
                new_access_token = AccessToken.for_user(user)
                new_refresh_token = RefreshToken.for_user(user)
                return Response({
                    'access': str(new_access_token),
                    'refresh': str(new_refresh_token),
                }, status=status.HTTP_200_OK)
            else:
                # Refresh token is valid; generate a new access token
                new_access_token = AccessToken.for_user(user)
                return Response({'access': str(new_access_token)}, status=status.HTTP_200_OK)

    # Access token is still valid
    return Response({'message': 'Access token is valid'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user_details(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'full_name': user.get_full_name(),
    }
    return Response(context)


@api_view(['GET'])
def get_products_list(request):
    response = []
    platform_id = int(request.GET['platform'])
    products = Product.objects.filter(platform=platform_id)
    for product in products:
        # response = []
        platform = Platform.objects.get(id=product.platform.id)
        if (platform_id == 1):
            print("hello")
            latest_date = ProductDetails.objects.filter(product=product, platform=platform, main_seller='Yes').aggregate(latest_date=Max('crawl_date'))['latest_date']
            print(latest_date)
            # return Response({"foo": "bar"})
            today_product_details = ProductDetails.objects.filter(product=product, platform=platform, main_seller='Yes', crawl_date=latest_date)
            # return Response(today_product_details.values())
            yesterday_product_details = ProductDetails.objects.filter(product=product, platform=platform, main_seller='Yes', crawl_date=latest_date - timedelta(days=1))
            # if (len(today_product_details) == 0):
            #     yesterday_product_details = ProductDetails.objects.filter(product=product, platform=platform, main_seller='Yes', crawl_date=datetime.now() - timedelta(days=2))
            #     today_product_details = ProductDetails.objects.filter(product=product, platform=platform, main_seller='Yes', crawl_date=datetime.now() - timedelta(days=1))
            #     print(len(today_product_details))

        else:
            yesterday_product_details = ProductDetails.objects.filter(product=product, platform=platform, crawl_date=datetime.now() - timedelta(days=1)).distinct('product_id')
            today_product_details = ProductDetails.objects.filter(product=product, platform=platform, crawl_date=datetime.now()).distinct('product_id')
            if (len(today_product_details) == 0):
                yesterday_product_details = ProductDetails.objects.filter(product=product, platform=platform, crawl_date=datetime.now() - timedelta(days=2)).distinct('product_id')
                today_product_details = ProductDetails.objects.filter(product=product, platform=platform, crawl_date=datetime.now() - timedelta(days=1)).distinct('product_id')

        # rating_data = ProductDetails.objects.filter(product=product, platform=platform, crawl_date=datetime.now()).distinct('product')
        # last_rating_data = ProductDetails.objects.filter(product=product, platform=platform, crawl_date=datetime.now() - timedelta(days=1)).distinct('product')
        # return Response(product_details)
        # return Response(product_details.values())
        for details in today_product_details:
            context = {}
            product_name = product.product_name
            context['product_id'] = details.product.id
            context['platform'] = platform.platform_name
            context['platform_id'] = platform.id
            context['product_name'] = product_name
            for data in yesterday_product_details:
                if (data.product == details.product and data.platform == details.platform and data.area == details.area):
                    # print("Something")
                    if (details.price > data.price):
                        context['change'] = 1
                        context['yesterday_price'] = data.price
                    elif (details.price == data.price):
                        context['change'] = 0
                        context['yesterday_price'] = data.price
                    else:
                        context['change'] = -1
                        context['yesterday_price'] = data.price
                # else:
                #     context['change'] = 2
                #     context['yesterday_price'] = 'No Data'
            context['seller'] = details.seller_name
            context['today_price'] = details.price
            context['date'] = details.crawl_date
            context['overall_rating'] = details.overall_rating
            context['product_details_id'] = details.id
            response.append(context)
    return Response(response)


@api_view(['GET'])
def get_products_rating(request):
    response = []
    platform = request.GET['platform_id']
    products = Product.objects.filter(platform=platform)
    for product in products:
        platform = Platform.objects.get(id=product.platform.id)
        latest_date = ProductDetails.objects.filter(product=product, platform=platform).aggregate(latest_date=Max('crawl_date'))['latest_date']
        today_list_data = ProductDetails.objects.filter(product=product, platform=platform, crawl_date=latest_date).distinct('product')
        yesterday_list_data = ProductDetails.objects.filter(product=product, platform=platform, crawl_date=latest_date - timedelta(days=2)).distinct('product')
        for data in today_list_data:
            context = {}
            
            context['product_name'] = product.product_name
            context['platform'] = platform.platform_name.title()
            context['current_rating'] = float(data.overall_rating)
            for yes in yesterday_list_data:
                if (yes.product == data.product):
                    context['last_rating'] = float(yes.overall_rating)
                    break
                else:
                    context['last_rating'] = 'No rating'
            response.append(context)

    return Response(response)
        # return Response(data.values())
    return Response({'foo': 'bar'})

@api_view(['GET'])
def get_product_details(request):

    product_id = request.GET['product_id']

    product_details = ProductDetails.objects.get(id=product_id)

    product_name = product_details.product.product_name
    product_platform = product_details.platform.platform_name
    product_brand = product_details.product.project_identifier.brand
    product_ratings = product_details.overall_rating
    product_total_rating = product_details.total_ratings
    product_five_stars_rating = product_details.five_stars_rating
    product_four_stars_rating = product_details.four_stars_rating
    product_three_stars_rating = product_details.three_stars_rating
    product_two_stars_rating = product_details.two_stars_rating
    product_one_star_rating = product_details.one_star_rating
    product_price = product_details.price
    product_availability = product_details.availability
    product_seller = product_details.seller_name
    product_main_seller = product_details.main_seller

    context = {
        'name': product_name,
        'platform': product_platform,
        'brand': product_brand,
        'ratings': product_ratings,
        'total_ratings': product_total_rating,
        'five_stars_rating': product_five_stars_rating,
        'four_stars_rating': product_four_stars_rating,
        'three_stars_rating': product_three_stars_rating,
        'two_stars_rating': product_two_stars_rating,
        'one_star_rating': product_one_star_rating,
        'price': product_price,
        'availability': product_availability,
        'seller': product_seller,
        'main_seller': product_main_seller,
    }

    return Response(context)

@api_view(['GET'])
def get_product_details_2(request):

    product_id = request.GET['product_id']
    platform = request.GET['platform_id']
    response = {}

    latest_date = ProductDetails.objects.filter(product=product_id, platform=platform).aggregate(latest_date=Max('crawl_date'))['latest_date']
    products = ProductDetails.objects.filter(product=product_id, platform=platform, crawl_date=latest_date)

    product_name = products[0].product.product_name
    product_platform = products[0].platform.platform_name
    product_brand = products[0].product.project_identifier.brand
    product_ratings = products[0].overall_rating
    product_total_rating = products[0].total_ratings
    product_five_stars_rating = products[0].five_stars_rating
    product_four_stars_rating = products[0].four_stars_rating
    product_three_stars_rating = products[0].three_stars_rating
    product_two_stars_rating = products[0].two_stars_rating
    product_one_star_rating = products[0].one_star_rating
    seller = []
    for product in products:
        product_price = product.price
        product_availability = product.availability
        product_seller = product.seller_name
        product_main_seller = product.main_seller
        context = {
            "price": product_price,
            "availability": product_availability,
            "seller": product_seller,
            "main_seller": product_main_seller
        }
        seller.append(context)
    response = {
        'name': product_name,
        'platform': product_platform,
        'brand': product_brand,
        'ratings': product_ratings,
        'total_ratings': product_total_rating,
        'five_stars_rating': product_five_stars_rating,
        'four_stars_rating': product_four_stars_rating,
        'three_stars_rating': product_three_stars_rating,
        'two_stars_rating': product_two_stars_rating,
        'one_star_rating': product_one_star_rating,
        'seller': seller
    }
    return Response(response)
    return Response({"foo": "bar"})

@api_view(['GET'])
def get_keyword_suggestions(request):
    response = []

    platform = request.GET['platform']
    duration = request.GET['duration']
    duration = time_range[int(duration)]
    print(duration)
    keyword = request.GET['keyword']

    keyword_result = KeywordSearchResult.objects.filter(platform=platform, keyword=keyword)
    for data in keyword_result:
        keyword_platform = data.platform.platform_name
        keyword_pincode = data.area.pincode
        # keyword_product_area_joint = ProductArea.objects.filter(area=keyword_pincode)[0]
        # keyword_product_id = keyword_product_area_joint.product
        # keyword_product_area = keyword_product_area_joint.area
        # keyword_product = keyword_product_id.product_name
        keyword_product = data.keyword.keyword
        keyword_product_name = data.product_name
        keyword_duration = data.crawl_date

        context = {
            "platform": keyword_platform,
            "product": keyword_product,
            "product_name": keyword_product_name,
            "duration": keyword_duration
        }
        response.append(context)
    return Response(response)
    return Response({"foo": "bar"})

@api_view(['GET'])
def get_keyword_list(request):
    keywords = KeywordTbl.objects.all()
    serializer = KeywordListSerializer(keywords, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_platform_list(request):
    platform = Platform.objects.all()
    serializer = PlatformListSerializer(platform, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_duration_list(request):
    context = {
        1: "Today",
        2: "Last 7 Days",
    }

    return Response(context)

@api_view(['GET'])
def get_brand_list(request):
    brand = ProjectIdentifier.objects.all()
    serializer = BrandListSerializer(brand, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_performance_product_list(request):

    response = []
    brand = request.GET['brand']
    products = Product.objects.filter(project_identifier=brand)
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)
    # for product in products:
    #     context = {}
    #     context['product_id'] = product.id
    #     context['product_name'] = product.product_name
    #     context['platform'] = product.platform.id
    #     context['platform_name'] = product.platform.platform_name.title()

    #     response.append(context)
    # return Response(response)
    # return Response({'foo':'bar'})

@api_view(['GET'])
def get_keyword_search_result(request):

    platform = request.GET['platform']
    duration = keyword_time_range[request.GET['duration']]
    keyword = request.GET['keyword']

    result = KeywordSearchResult.objects.filter(platform=platform, crawl_date__gte=datetime.now() - duration, keyword=keyword)
    serializer = KeywordSearchResultSerializer(result, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def get_keyword_filtered_data(request):

    arr = request.data['arr']
    arr = map(int, arr)

    result = KeywordSearchResult.objects.filter(id__in=arr)
    df = pd.DataFrame(list(result))

    excel_buffer = BytesIO()

    df.to_excel(excel_buffer, index=False)

    response = HttpResponse(excel_buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    return response
    # print(result)
    serializer = KeywordFilterDataSerializer(result, many=True)
    return Response(serializer.data)

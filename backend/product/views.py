from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import CustomUser, Product, Platform, ProductDetails
from .serializers import ProductDetailsPlatformSerializer

# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your views here.
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
    platform = request.GET['platform']
    products = Product.objects.filter(platform=platform)
    for product in products:
        response = []
        platform = Platform.objects.get(id=product.platform.id)
        product_details = ProductDetails.objects.filter(product=product, platform=platform)
        for details in product_details:
            context = {}
            product_name = product.product_name
            context['platform'] = platform.platform_name
            context['product_name'] = product_name
            context['price'] = details.price
            context['date'] = details.crawl_date
            context['overall_rating'] = details.overall_rating
            context['product_details_id'] = details.id
            response.append(context)
    return Response(response)

@api_view(['GET'])
def get_product_details(request):

    product_id = request.GET['product_id']

    product_details = ProductDetails.objects.get(id=product_id)

    product_name = product_details.product.product_name
    product_platform = product_details.platform.platform_name
    product_brand = product_details.product.project_identifier.brand
    product_ratings = product_details.overall_rating
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

from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.urls.authtoken')),
    path('user_login/', views.user_login, name='user-login'),
    path('check_access_token/', views.check_access_token, name='check-access-token'),
    path('get_user_details/', views.get_user_details, name='get-user=details'),
    path('get_products_list/', views.get_products_list, name='get-products-list'),
    path('get_products_rating/', views.get_products_rating, name='get-product-rating'),
    path('get_product_details/', views.get_product_details, name='get-product-details'),
    path('get_product_details_2/', views.get_product_details_2, name='get-product-details-2'),
    path('get_keyword_suggestions/', views.get_keyword_suggestions, name='get-keyword-suggestions'),
    path('get_keyword_list/', views.get_keyword_list, name='get-keyword-list'),
    path('get_platform_list/', views.get_platform_list, name='get-platform-list'),
    path('get_duration_list/', views.get_duration_list, name='get-duration-list'),
    path('get_brand_list/', views.get_brand_list, name='get-brand-list'),
    path('get_keyword_search_result/', views.get_keyword_search_result, name='get-keyword-search-result'),
    path('get_keyword_filtered_data/', views.get_keyword_filtered_data, name='get-keyword-filtered-data'),
    path('get_performance_product_list/', views.get_performance_product_list, name='get-performance-product-list'),
]

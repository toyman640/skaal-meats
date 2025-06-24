from django.urls import path
from frontend import views


app_name= 'frontend'


urlpatterns = [
  path('about-us/', views.about_us_view, name='about_us_view'),
  path('contact-us/', views.contact_us_view, name='contact_us_view'),
  path('pricing/', views.shop_view, name='shop_view'),
]
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('register',views.register, name="register"),
    path('login/',views.loginpage, name="login"),
    path('logout/',views.logutUser, name="logout"),
    #path('product/',views.ProductView.as_view(), name="product"),
    path('category/<slug:val>',views.CategoryView.as_view(), name="category"),
    path('category-title/<val>', views.CategoryTitle.as_view(), name="category-title"),
    path('product-detail/<int:pk>',views.ProductDetail.as_view(), name="product-detail"),
    path('profile/',views.ProfileView.as_view(), name="profile"),
    path('add-to-cart/',views.add_to_cart, name="add-to-cart"),
    path('cart/',views.show_cart, name="showcart"),
    path('checkout/',views.checkout, name="checkout"),
    path('remove-from-cart/',views.remove_from_cart, name="remove-from-cart"),
    path('plus-to-cart/',views.plus_to_cart, name="plus-to-cart"),
    path('order/',views.order, name="order"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
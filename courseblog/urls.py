
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.homepage, name="home"),
    #path('contact/', views.contactpage, name="contact"),
    path('courses/', views.coursespage, name="courses"),
    #path('about-us/', views.aboutuspage, name="about-us"),
    path('meeting/', views.videocall, name="meeting"),
    path('courses/<slug:course_slug>/', views.course_details, name='course-detail'),
    path('create_course/', views.createCourse, name="create_course"),
    path('update_course/<slug:course_slug>/', views.updateCourse, name="update_course"),
    path('delete_course/<slug:course_slug>/', views.deleteCourse, name="delete_course"),
    path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<slug:course_slug>/', views.updateProduct, name="update_product"),
    path('delete_product/<slug:course_slug>/', views.deleteProduct, name="delete_product"),
    #path('shop/', views.shoppage, name="shop"),
    #path('cart/', views.cart, name = 'cart'),
    #path('checkout/', views.checkout, name = 'checkout'),
    #path('updatecart/', views.updateCart),
    #path('updatequantity/', views.updateQuantity),
    #path('payment', views.payment, name = 'payment'),
    #path('order/', views.orderpage, name='order'),
    path('accounts/', include('allauth.urls')),
    
]




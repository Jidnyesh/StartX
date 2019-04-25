from django.contrib import admin
from django.urls import path,include
from startx import views

urlpatterns = [
    path('',views.index,name="index"),

    #User authentication
    path('home/',views.home,name="home"),
    path('home/<int:instance_id>',views.product_detail,name="product_detail"),
    path('home/<int:instance_id>/like',views.likes,name="likes"),
    path('home/add_product',views.addproduct,name="addproduct"),
    path('home/logout',views.logoutv,name="logoutv"),
    path('user-login',views.loginv,name = "loginv"),

    #User profile
    path('home/profile',views.profile,name="profile"),
    path('home/profile/<int:instance_id>/dashboard',views.dashboard,name="dashboard"),
    path('home/profile/profile',views.profile_public_profile,name="profile_public_profile"),
    path('home/profile/setting',views.profile_setting,name="profile_setting"),
    path('home/profile/product',views.profile_product,name="profile_product"),
    path('home/profile/jobs',views.profile_jobs,name="profile_jobs"),
    path('home/profile/stock',views.profile_stock,name="profile_stock"),

    #Categories
    path('home/categories',views.product_categories,name="product_categories"),
    path('home/categories/Technology',views.technology_category,name="technology_category"),
    path('home/categories/Vehicles',views.vehicle_category,name="vehicle_category"),
    path('home/categories/Sports',views.sports_category,name="sports_category"),
    path('home/categories/Audio',views.audio_category,name="audio_category"),
    path('home/categories/Furniture',views.furniture_category,name="furniture_category"),
    path('home/categories/Clothing',views.clothing_category,name="clothing_category"),

    #jobs
    path('home/jobs',views.jobs,name = "jobs"),
    path('home/jobs/create',views.add_jobs,name="add_jobs"),
    path('home/jobs/<int:instance_id>',views.job_detail,name="job_detail"),

    #Advertisement
    path('home/advertisement',views.advertisement,name="advertisement"),
    path('home/advertisement/add',views.add_advertisement,name="add_advertisement"),

    #Guide
    path('home/guide',views.guide , name="guide"),


]

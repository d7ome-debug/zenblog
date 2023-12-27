from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('post', views.post, name='post'),
    path('category', views.category, name='category'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
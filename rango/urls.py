from django.urls import path
from django.conf.urls import url
from rango import views
from rango import about
from rango.views import AboutView, AddCategoryView, ProfileView

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('search/', views.search, name='search'),
    path('goto/', views.goto_url, name='goto'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('profile/<username>/', ProfileView.as_view(), name='profile'),
    path('profiles/', views.list_profiles, name='list_profiles'),
]
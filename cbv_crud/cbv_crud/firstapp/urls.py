from . import views
from django.urls import path

urlpatterns = [
    path('',views.HomeView.as_view(),name = 'home'),
    path('showprod/', views.Laptoplistview.as_view(), name = 'allprods'),
    path('allprod/', views.LaptopCreateView.as_view(), name = 'addprod'),
    path('update/<int:pk>',views.LaptopUpdateView.as_view(),name='updt'),
    path('delete/<int:pk>',views.LaptopUpdateView.as_view(),name='del'),
]
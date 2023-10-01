from django.urls import path
from card_app import views

app_name = "card_app"



urlpatterns = [
    path('', views.CompanyList.as_view(), name = 'list'),
    path('<int:pk>', views.CompanyDetailView.as_view(),name = 'detail'),
    path('create', views.CompanyCreateView.as_view(), name = 'create'),
    path('update/<int:pk>', views.CompanyUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>',views.CompanyDeleteView.as_view(), name = 'delete'),
    path('p_update/<int:pk>', views.ProductsUpdateView.as_view(), name = 'p_update'),
    path('p_create', views.ProductsCreateView.as_view(), name = "p_create"),    
    path('p_delete/<int:pk>', views.ProductDeleteView.as_view(), name = 'p_delete'),
    path('product_details/<int:pk>', views.ProductDetailView.as_view(),name = 'p_detail')
]


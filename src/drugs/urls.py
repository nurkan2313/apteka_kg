from django.urls import path
from drugs import views

urlpatterns = [
    path('drugs/', views.snippet_list),
    path('drugs/<int:pk>/', views.snippet_detail),
]
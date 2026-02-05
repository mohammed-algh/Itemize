from django.urls import path
from .views import HomeView, AddItemView, ItemDetailView, ItemUpdateView, ItemDeleteView
from django.shortcuts import redirect

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AddItemView.as_view(), name='add_item'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('item/<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]
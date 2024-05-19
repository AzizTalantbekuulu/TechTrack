from django.urls import path
from .views import RegisterView, LoginView, UserListCreateView, UserDetailView, EquipmentListCreateView, EquipmentDetailView, DataListCreateView, DataDetailView, AlertListCreateView, AlertDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('equipment/', EquipmentListCreateView.as_view(), name='equipment-list'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('equipment/<int:equipment_id>/data/', DataListCreateView.as_view(), name='data-list'),
    path('equipment/<int:equipment_id>/data/<int:pk>/', DataDetailView.as_view(), name='data-detail'),
    path('equipment/<int:equipment_id>/alerts/', AlertListCreateView.as_view(), name='alert-list'),
    path('equipment/<int:equipment_id>/alerts/<int:pk>/', AlertDetailView.as_view(), name='alert-detail'),
]

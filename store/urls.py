from django.urls import path
from .import views


urlpatterns = [
    path("add-equipment-list/", views.addEquipmentList, name="add-equipment-list"),
    path("edit-equipment-list/<int:pk>/", views.editEquipmentList, name="edit-equipment-list"),
    path("delete-equipment-list/<int:pk>/", views.deleteEquipmentList, name="delete-equipment-list"),
    path('download/<int:pk>/', views.download, name="download"),
    path("specification/<int:pk>/",views.specification, name="specification"),
    path("index", views.index, name="index"),
    path("", views.logIn, name="login"),
]

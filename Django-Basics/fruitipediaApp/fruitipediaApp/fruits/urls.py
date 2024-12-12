from django.urls import path, include

from fruitipediaApp.fruits import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-fruit/', views.CreateFruit.as_view(), name='create fruit'),
    path('<int:fruit_id>/', include([
        path('details-fruit/', views.details_fruit, name='details fruit'),
        path('edit-fruit/', views.FruitEditView.as_view(), name='edit fruit'),
        path('delete-fruit/', views.delete_fruit, name='delete fruit'),
    ])),
    path('create-category/', views.create_category, name='create category'),
]

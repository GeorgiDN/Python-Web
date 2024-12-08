from django.urls import path, include

from fruitipediaApp.fruits import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-fruit/', views.create_fruit, name='create fruit'),
    path('<int:fruit_id>/', include([
        path('details-fruit/', views.details_fruit, name='details fruit'),
        path('edit-fruit/', views.edit_fruit, name='edit fruit'),
        path('delete-fruit/', views.delete_fruit, name='delete fruit'),
    ])),
    path('create-category/', views.create_category, name='create category'),
]

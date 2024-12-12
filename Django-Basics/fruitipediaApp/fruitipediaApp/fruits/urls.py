from django.urls import path, include

from fruitipediaApp.fruits import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create-fruit/', views.CreateFruit.as_view(), name='create fruit'),
    path('<int:fruit_id>/', include([
        path('details-fruit/', views.details_fruit, name='details fruit'),
        path('edit-fruit/', views.FruitEditView.as_view(), name='edit fruit'),
        path('delete-fruit/', views.FruitDeleteView.as_view(), name='delete fruit'),
    ])),
    path('create-category/', views.CategoryCreateView.as_view(), name='create category'),
]

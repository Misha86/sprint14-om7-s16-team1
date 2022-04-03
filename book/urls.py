from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.book_list, name='book-list'),
    path('<int:id>/', views.book, name='book'),
]
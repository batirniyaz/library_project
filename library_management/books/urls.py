from django.urls import path
from .views import BookListApiView, book_list_view

urlpatterns = [
    path('', BookListApiView.as_view()),
    path("book/", book_list_view)
]
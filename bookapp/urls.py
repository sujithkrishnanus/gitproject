from django.urls import path
from .import views

urlpatterns = [
        path('createbook',views.createBook, name='createbook'),

        path('',views.listView, name='booklist'),

        path('update/<int:book_id>/',views.updateBook, name='update'),

        path('detail/<int:book_id>/',views.detailsBook, name='details'),

        path('delete/<int:book_id>/',views.deleteBook, name='delete'),

        path('author/',views.CreateAuthor, name='author'),

        path('index/',views.index),

        path('searchbook/', views.searchBook, name='searchbook'),


]
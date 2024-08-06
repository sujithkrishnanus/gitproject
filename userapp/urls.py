from django.urls import path
from .import views

urlpatterns = [

# user interface path
    path('',views.listView, name='list_view'),

    path('detail_view/<int:book_id>',views.detailsBook, name='detail_view'),

    path('search_book',views.searchBook,name='search_book'),

# cart design path

    path('add_to_cart/<int:book_id>/',views.add_to_cart,name='add_to_cart'),

    path('viewcart/',views.view_cart,name='viewcart'),

    path('increase_quantity/<int:item_id>/', views.increase_quantity,name='increase_quantity'),

    path('decrease_quantity/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),

    path('remove_cart/<int:item_id>/', views.remove_from_cart, name='remove_cart'),

# Gateway design path

    path('create_checkout/', views.create_checkout_session, name='create_checkout'),

    path('success/', views.success, name='success'),

    path('cancel/',views.success, name='cancel')

]
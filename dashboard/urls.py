from django.urls import path

from .views import (pc_delete_view, playable_characters_view, pc_list_view,
                    dashboard_view, pc_inventory_view, item_view,
                    item_delete_view, item_edit_view)


app_name = 'dashboard'
urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('playable_characters/', playable_characters_view,
         name='playable_characters'),
    path('pc_list/', pc_list_view, name='pc_list'),
    path('pc_delete/<pk>/', pc_delete_view, name='pc_delete'),
    path('pc_list/<pk>/inventory/', pc_inventory_view, name='pc_inventory'),
    path('pc_list/<pk>/inventory/item/', item_view, name='item'),
    path('pc_list/<pk>/inventory/item/delete/<pk_item>',
         item_delete_view, name='item_delete'),
    path('pc_list/<pk>/inventory/item/edit/<pk_item>',
         item_edit_view, name='item_edit')

]

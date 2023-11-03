from django.urls import path
from main.views import show_main
from main.views import create_product, show_xml, show_main, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, edit_product, delete_product
from main.views import get_product_json, add_product_ajax


app_name = 'main'

urlpatterns = [
    path('create_product', create_product, name='create_product'),
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete/<int:id>', delete_product, name='delete_product'),
    path('get-product/', get_item_json, name='get_item_json'),
    path('create-product-ajax/', add_item_ajax, name='add_product_ajax'),
]


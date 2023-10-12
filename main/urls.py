from django.urls import path
from main.views import show_main, create_product, delete_item, show_xml, show_json, show_xml_by_id, show_json_by_id, reduce_amount, increase_amount, get_product_json, add_product_ajax, increase_amount_ajax, get_updated_data, delete_item_ajax
from main.views import register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'),
    path('reduce_amount/<int:id>/', reduce_amount, name='reduce_amount'),
    path('increase_amount/<int:id>/', increase_amount, name='increase_amount'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('xml/', show_xml, name='show_xml'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('get-updated-data/', get_updated_data, name='get_updated_data'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('increase_amount_ajax/<int:id>/', increase_amount_ajax, name='increase_amount_ajax'),
    path('delete_item_ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),

]

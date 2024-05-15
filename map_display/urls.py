# In urls.py (of your app)

from dal import autocomplete
from django.urls import path
from .views import *

urlpatterns = [
 

    path('electric-poles/', electric_poles_map, name='electric_poles_map'),
    # path('connected-poles-map/', connected_poles_map, name='connected_poles_map'),
    path('electric-poles-map/', electric_poles_map, name='electric_poles_map'),
    path('get-connected-poles/', get_connected_poles, name='get_connected_poles'),

]   

from django.urls import path
from main.views import show_main, create_menfess_form

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add/', create_menfess_form, name='create_menfess_form')
]
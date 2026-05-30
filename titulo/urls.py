from django.urls import include, path
from . import views

app_name = 'titulo'

urlpatterns = [
     path('listar/', views.listar, name='listar'),
     path('cadastrar/', views.cadastrar, name='cadastrar'),
   
]


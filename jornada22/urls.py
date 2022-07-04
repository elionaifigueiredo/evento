from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inscricao', views.add_inscrito, name="add_inscrito"),
    path('generate-pdf', views.generate_pdf, name='generate-pdf')
]

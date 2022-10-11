from django.urls import path, include
from . import views


urlpatterns = [
    path('advocates', views.get_all_advocates, name='advocates'),
    path('advocates/<int:id>', views.get_advocate, name='advocate'),
    path('companies', views.get_all_companies, name='companies'),
    path('companies/<int:id>', views.get_company, name='company'),
]
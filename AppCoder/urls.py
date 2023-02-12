from django.urls import path
from AppCoder.views import inicio, curso, profesores, entregables, estudiantes

urlpatterns = [
    path('inicio/', inicio),
    path('curso/', curso),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
]

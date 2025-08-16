from django.urls import path
from .views import keyword
urlpatterns=[
    path('flex/', keyword),
]
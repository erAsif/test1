from django.urls import path,include
from .views import myText

urlpatterns = [
    path('myText/', myText ,name="myText"),

]
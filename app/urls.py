from django.urls import path
from .views import MailingViewSet,ClientViewSet

app_name = "app"
urlpatterns = [
    path('mailing/' , MailingViewSet.as_view(), name = 'mailnig'),
    path('client/' ,ClientViewSet.as_view(), name ='client'),

  


]
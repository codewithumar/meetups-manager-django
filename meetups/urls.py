from . import views
from django.urls import path


urlpatterns=[
    path('',views.index,name='index'),
    path('meetup/success',views.confirmation_registration,name='meetup-success'),
    path('meetup-detail/<slug:meetup_slug>',views.meetup_details,name='meetup-detail')
]
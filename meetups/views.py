from django.shortcuts import render
from .models import Meetup
from .forms import RegistrationForm


# Create your views here.

def index(request):


    meetups=Meetup.objects.all()
    return render(request,'templetes\index.html',{'meetups':meetups})

def meetup_details(request,meetup_slug):
    try:
        selected_meetup=Meetup.objects.get(slug=meetup_slug)
        registration_form=RegistrationForm()
        return render(
            request,
            'templetes\meetup-details.html',
            {'meetup_found':True ,
            'meetup':selected_meetup,
            'form':registration_form
            })
    except Exception as exp:
        return render(request,
                      'templetes\meetup-details.html',
                      {'meetup_found':False
                       })

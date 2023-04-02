from django.shortcuts import render
from .models import Meetup


# Create your views here.

def index(request):


    meetups=Meetup.objects.all()
    return render(request,'templetes\index.html',{'meetups':meetups})

def meetup_details(request,meetup_slug):
    try:
        selected_meetups=Meetup.objects.get(slug=meetup_slug)
        return render(
            request,
            'templetes\meetup-details.html',
            {'meetup_found':True,
             'meetup_title':selected_meetups.title,
            'meetup_description':selected_meetups.description,
            'meetup_slug':meetup_slug
            })
    except Exception as exp:
        return render(request,
                      'templetes\meetup-details.html',
                      {'meetup_found':False
                       })

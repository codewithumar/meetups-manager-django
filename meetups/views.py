from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    meetups=[
        {'title':'First Meetup',
         'details':'lorem lorem lorem lorem lorem lorem lorem lorem',
         'slug':'a-first-meetup',
         'location':'pakistan'
        },
        {'title':'First Meetup',
         'details':'lorem lorem lorem lorem lorem lorem lorem lorem',
         'slug':'a-second-meetup',
         'location':'pakistan'
        },
        {'title':'First Meetup',
         'details':'lorem lorem lorem lorem lorem lorem lorem lorem',
         'slug':'a-third-meetup',
         'location':'pakistan'
        }
    ]
    return render(request,'templetes\index.html',{'meetups':meetups})

def meetup_details(request,meetup_slug):
    
    selected_meetups={
        'title':'first meeetup',
        'description':' this is first meetup'              
        }
    return render(
        request,
        'templetes\meetup-details.html',
        {'meetup_title':selected_meetups['title'],
         'meetup_description':selected_meetups['description'],
         'meetup_slug':meetup_slug
        })
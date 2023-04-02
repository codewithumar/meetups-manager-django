from django.shortcuts import render,redirect
from .models import Meetup,Participant
from .forms import RegistrationForm


# Create your views here.

def index(request):


    meetups=Meetup.objects.all()
    return render(request,'templetes\index.html',{'meetups':meetups})

def meetup_details(request,meetup_slug):
    try:
        selected_meetup=Meetup.objects.get(slug=meetup_slug)
        if request.method =='GET':
            registration_form=RegistrationForm()
        elif request.method=='POST':
            registration_form=RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email=registration_form.cleaned_data['email']
                participant,_=Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('meetup-success',meetup_slug=meetup_slug)

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

def confirmation_registration(request):

    return render( 
        request, 
        'templetes/registration-success.html',
       # {'organizer_email':meetup.organizor_email}
        )
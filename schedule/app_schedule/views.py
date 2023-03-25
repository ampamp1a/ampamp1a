from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from app_select.models import Subjects_Test_Date
from app_schedule.models import Subjects_info , User_subjects
from app_select.views import start_times,user_data
from django.db.models import Q

# Create your views here.
@login_required(login_url='login')
def schedule_view(request):
    sub_date = Subjects_Test_Date.objects.all()
    sub_objects = Subjects_info.objects.all()
    user_id = request.user.id
    user = User_subjects.objects.filter(user_id_id = user_id)

    day_start_times_used = user_data[user_id]['day_start_times_used']
    
    days = {
    "M": "Monday",
    "T": "Tuesday",
    "W": "Wednesday",
    "H": "Thursday",
    "F": "Friday",
    "S": "Sunday",
}
    
    # The select button was clicked
    subject_id = request.POST.get('id')
    # insert name into user table using Django ORM
    User_subjects.objects.create(user_id_id=user_id, sub_id_id=subject_id)

    context = {'sub_date':sub_date, 
               'sub_objects':sub_objects,
               'users':user,
               'start_times':start_times,
               'day_start_times_used':day_start_times_used,
               'days':days}
    
    return render(request, 'schedule.html' , context)

def about(request):
    return render(request, 'about.html')

#1 searchandshow
def Show_sub(request):
    # search btn
    if 'q' in request.GET:
        search = request.GET['q']
        multiple_search = Q(Q(name__icontains=search) | Q(code__icontains=search) )
        sub_name = Subjects_info.objects.filter(multiple_search)
    else:
        sub_name = Subjects_info.objects.none()
        
    users = User_subjects.objects.all()    
    context = {'sub_name':sub_name,
                'users':users,
}        
    return render(request,'showsub.html',context)

#2 showandcount
def Show_subregis(request):
    sub_objects = Subjects_info.objects.all()
    users = User_subjects.objects.all()

    context = {'sub_objects':sub_objects,
               'users':users,
}
    return render(request,'showsubregis.html',context)

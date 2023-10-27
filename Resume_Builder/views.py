from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import  messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, models
from django.contrib.auth import login as login2
from django.contrib.auth.forms import AuthenticationForm

from django.db import IntegrityError
# from django.contrib.auth.models import user_data


def form_page1(request):
    return render(request, "form1.html",{'id':request.GET.get('id','1')})

def signup_page(request):
    return render(request, 'signup.html')

def login(request):
    return render(request,"login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')
    
def user_login(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        user = authenticate ( name=name,username=email, password=password )
        print()
        print("correct 123")
        print(user)
        if user is not None:
            print(name,email,password)
            print("correct")
            login2(request, user)
            email=user.email
            return render(request, 'display.html' ,{'email': email}) 
        else:
            print("incorrect 1")
            messages.error(request,'You enter wrong email or password')
            print(email,password)
            # form = AuthenticationForm(data=request.POST)
            return render(request, 'login.html')
    else:
        form = AuthenticationForm()
        print("incorrect 2")
        return render(request, 'signup.html', {'form': form})
    


def user_signup(request):
    users = models.User.objects.all()
    print(users)
    try:
        if request.method=="POST":
                name=request.POST.get('name','')
                email=request.POST.get('email','')
                password=request.POST.get('password','') 
                print(name,email,password)
                data=models.User.objects.create(first_name=name,email=email,password=password,username=email)
                data.set_password(password)
                data.save()
                messages.success(request,'Successfully signed in ')
                return render(request,"login.html")
    except IntegrityError :
        messages.error(request,'Somthing went wrong')
        return render(request,"signup.html")


def display_page(request):
    d = request.POST
    name = d.get('name','')
    profession=d.get('profession','')
    dob=d.get('dob','')
    contact_no=d.get('contact-no','')
    email=d.get('email','')
    profile=d.get('profile','')
    address=d.get('address','')
    linkedin=d.get('linkedin','')
    certificates=d.get('certificates','').split(',')
    projects=d.get('projects','').split(',')
    company=d.get('company','')
    job_duration=d.get('job-duration','')
    job_post=d.get('job-post','')
    job_about=d.get('job-about','')
    school_10=d.get('10-school','')
    grade_10=d.get('10-grade','')
    year_10=d.get('10-year','')
    school_12=d.get('12-school','')
    grade_12=d.get('12-grade','')
    year_12=d.get('12-year','')
    college=d.get('college','')
    college_grade=d.get('college-grade','')
    college_year=d.get('college-year','')
    skills=d.get('skills','').split(',')

    context = {
        'name':name,
        'profession':profession,
        'dob':dob,
        'contact_no':contact_no,
        'email':email,
        'address':address,
        'profile':profile,
        'linkedin':linkedin,
        'certificates':certificates,
        'projects':projects,
        'company':company,
        'job_duration':job_duration,
        'job_post':job_post,
        'job_about':job_about,
        'school_10':school_10,
        'grade_10':grade_10,
        'year_10':year_10,
        'school_12':school_12,
        'grade_12':grade_12,
        'year_12':year_12,
        'college':college,
        'college_grade':college_grade,
        'college_year':college_year,
        'skills':skills
    }

    templateId = request.GET.get('id','1')
    template_name = ""
    if templateId == '1':
        template_name = "resume1.html"
    elif templateId == '2':
        template_name = "resume2.html"
    elif templateId == '3':
        template_name = "resume3.html"
    else:
        template_name = "resume4.html"    

    
    return render(request,template_name,context)


def resume1(request):
    if request.method == "POST":
        name=request.POST.get('name','')
        profession=request.Post.get('profession','')
        dob=request.Post.get('dob','')
        contact=request.Post.get('contact_no','')
        print(name,profession,dob,contact)
    return render(request, "resume1.html",name,profession,dob,contact)
    # return render(request, "resume1.html")

def resume2(request):
    return render(request, "resume2.html")

def resume3(request):
    return render(request, "resume3.html")

def resume4(request):
    return render(request, "resume4.html")

def create_resume(request):
    if request.method == "POST":
        name=request.POST.get('name','')
        profession=request.Post.get('profession','')
        dob=request.Post.get('dob','')
        contact=request.Post.get('contact_no','')
        print(name,profession,dob,contact)
    return render(request, "resume1.html",fname,profession,dob,contact)
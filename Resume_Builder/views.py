from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import  messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, models
from django.contrib.auth import login as login2
from django.contrib.auth.forms import AuthenticationForm

from django.db import IntegrityError
import bleach
# from django.contrib.auth.models import user_data

class Job:
    def __init__(self,job_post='',job_about='',company='',job_duration=''):
        self.job_post = job_post
        self.job_about= job_about
        self.company = company
        self.job_duration = job_duration

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
            # return render(request, 'display.html' ,{'email': email}) 
            return render(request, 'selector.html')
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


def display_page(request):     #for fresher candidates
    d = request.POST
    objective = d.get('objective','')

    name = d.get('name','')  
    contact_no=d.get('contact_no','')
    # profession=d.get('profession','')
    address=d.get('address','')
    # dob=d.get('dob','')
    email=d.get('email','')
    linkedin=d.get('linkedin','')

    school_10=d.get('10-school','')
    grade_10=d.get('10-grade','')
    year_10=d.get('10-year','')
    school_12=d.get('12-school','')
    grade_12=d.get('12-grade','')
    year_12=d.get('12-year','')
    course_name=d.get('course_name','')
    college=d.get('college','')
    college_grade=d.get('college-grade','')
    college_year=d.get('college-year','')

    projects = request.POST.getlist('projects')

    skills = request.POST.getlist('skills')

    certificates = request.POST.getlist('certificates')
    
    

    context = {
        'objective' :objective,
        'name':name,
        # 'profession':profession,
        # 'dob':dob,
        'contact_no':contact_no,
        'email':email,
        'address':address,
        # 'profile':profile,
        'linkedin':linkedin,
        'certificates':certificates,
        'projects':projects,
        'school_10':school_10,
        'grade_10':grade_10,
        'year_10':year_10,
        'school_12':school_12,
        'grade_12':grade_12,
        'year_12':year_12,
        'course_name':course_name,
        'college':college,
        'college_grade':college_grade,
        'college_year':college_year,
        'skills':skills
    }
    print(context)
    templateId = request.GET.get('id','1')
    template_name = ""
    if templateId == '1':
        template_name = "fresher_resume1.html"
    elif templateId == '2':
        template_name = "fresher_resume2.html"
    elif templateId == '3':
        template_name = "fresher_resume3.html"
    else:
        template_name = "fresher_resume4.html"    

    
    return render(request,template_name,context)


def experiencedisplay_page(request):     #for experianed candidates
    d = request.POST
    print("dhruv")
    print(d.keys())
    print(d.values())
    image= d.get('image','')
    objective = d.get('objective','')
    name = d.get('name','')  
    contact_no=d.get('contact_no','')
    profession=d.get('profession','')
    address=d.get('address','')
    # dob=d.get('dob','')
    email=d.get('email','')
    linkedin=d.get('linkedin','')

    school_10=d.get('school_10','')
    grade_10=d.get('grade_10','')
    year_10=d.get('year_10','')
    school_12=d.get('school_12','')
    grade_12=d.get('grade_12','')
    year_12=d.get('year_12','')
    course_name=d.get('course_name','')
    college=d.get('college','')
    college_grade=d.get('college_grade','')
    college_year=d.get('college_year','')
    
    # projects = []
    # i = 1
    # while f"projectName{i}" in d.keys():
    #     projectName=d.get(f"projectName{i}",'')
    #     projectDiscription=d.get(f'projectDiscription{i}','')
    #     technologiesUsed=d.get(f'technologiesUsed{i}','')
    #     projects.append(project(projectName,projectDiscription,technologiesUsed))
    #     i+=1
    
    # print(projects)
    
    jobs = []
    i = 1
    while f"job_post{i}" in d.keys():
        company=d.get(f"company{i}",'')
        job_duration=d.get(f'job_duration{i}','')
        job_post=d.get(f'job_post{i}','')
        job_about=d.get(f'job_about{i}','')
        jobs.append(Job(job_post,job_about,company,job_duration))
        i+=1
    
    print(jobs)
    # skills=d.get('skills','').split(',')
    skills = request.POST.getlist('skills')

    # certificates=d.get('certificates','').split(',')
    certificates = request.POST.getlist('certificates')
    projects = request.POST.getlist('projects')


    context = {
        'image':image,
        'objective': objective,
        'name':name,
        'profession':profession,
        'contact_no':contact_no,
        'email':email,
        'address':address,
        'linkedin':linkedin,
        'certificates':certificates,
        'projects':projects,
        'jobs': jobs,
        'school_10':school_10,
        'grade_10':grade_10,
        'year_10':year_10,
        'school_12':school_12,
        'grade_12':grade_12,
        'year_12':year_12,
        'course_name':course_name,
        'college':college,
        'college_grade':college_grade,
        'college_year':college_year,
        'skills':skills
    }
    print(context)
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


def selector_page(request):
    return render(request,"selector.html")

def fresher_form(request):
    return render(request,"fresher.html", {"id":request.GET["id"]})

def experience_form(request):
    return render(request,"experience.html", {"id":request.GET["id"]})

def freshertemplate_page(request):
    return render(request,"freshertemplate.html")

def experiencetemplate_page(request):
    return render(request,"experiencetemplate.html")

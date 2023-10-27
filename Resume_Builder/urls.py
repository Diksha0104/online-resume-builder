"""Resume_Builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Resume_Builder import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('form1', views.form_page1,name="form_page1"),
    path('', views.signup_page,name="signup"),
    path('login/',views.login,name="login"),
    path('user_signup/',views.user_signup,name="user_signup "),
    path('user_login/',views.user_login,name="user_login"),
    path('logout_view',views.logout_view,name="user_logout"),
    # path('', include("App.urls")),
    path('display_page',views.display_page,name="display_page"),
    path('resume1',views.resume1,name="resume1"),
    path('resume2.html',views.resume2,name="resume2"),
    path('resume3.html',views.resume3,name="resume3"),
    path('resume4.html',views.resume4,name="resume4"),

]

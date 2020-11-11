Views.Py
from django.views.generic import TemplateView
from .models import Register
from .forms import Registerform
from django.http import HttpResponse
#Login and registration page
class HomePageView(TemplateView):
    template_name = 'register.html'
    
    
    # when submit button on html then perform action to post data in database .. it calls forms.py
    def post(self,request):
        form=Registerform(request.POST.get(s))
        print('Enter to post method')
        if(form.is_valid(commit=false)):
            r=Register(name=name, phno=phno, pswd=pswd)
            name=form.cleaned_data['name']
            phone_number=form.cleaned_data['phno']
            password=form.cleaned_data['pswd']
            r.save()
            return HttpResponse('Success')
        args = {'form':form, 'name':name, 'phno':phno, 'pswd':pswd}
        return render(request,'cropwiseanalysis.html',args)


# Service Providing pages
class ServicePageView(TemplateView):
    template_name='cropwiseanalysis.html'



Models.py:
	
from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=30)
    phno=models.CharField(max_length=10)
    pswd=models.CharField(max_length=15)
    
app/prices/urls.py
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns=[
    path('',views.HomePageView.as_view(),name='register'),
    path('cropwiseanalysis/',views.ServicePageView.as_view(),name='cropwiseanalysis'),

]

app/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pricess.urls')),
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

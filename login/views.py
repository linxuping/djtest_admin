#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from login.models import User
from django import forms
from django.forms import ModelForm
from django.template import Template,Context,RequestContext
from django.views.decorators.csrf import csrf_exempt

def hello(request):
  return HttpResponse("hello,world")

#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
class ContactForm(ModelForm):
  class Meta:
    model = User
    fields = ('username', 'password')
	
#登录
@csrf_exempt
def login(request):
    uf = None
    if request.method == 'POST':
        print "-------login--------"
        uf = ContactForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            print "+++ ",username, password
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                return render_to_response('success.html',{'username':username})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = ContactForm()
    #return render_to_response('login.html',{'uf':uf})
    return render_to_response('login.html',{"uf":uf},context_instance=RequestContext(request))

from django.contrib.auth import authenticate	
from django.contrib.auth import login as adminlogin
from django.contrib.auth import logout as adminlogout
#登录
@csrf_exempt
def login1(request):
    print "+login1: ",request.user," + ",request.POST
    uf = None
    if request.method == 'POST':
        uf = ContactForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            #user = User.objects.filter(username__exact = username,password__exact = password)
            user = authenticate(username=username, password=password)
            if request.POST.get("extra", None) == "logout":
              print "-------------logout------------------>"
              adminlogout(request)
            elif None!=user and user.is_active:
              print "-------------login------------------>"
              adminlogin(request, user)
            print "+++ ", user, username, password
            if user is not None:
                return render_to_response('success.html',{'username':username})
            else:
                return HttpResponseRedirect('/login1/')
    else:
        uf = ContactForm()
	  
	  
    #return render_to_response('login1.html',{'uf':uf})
    return render_to_response('login1.html',{"uf":uf},context_instance=RequestContext(request))
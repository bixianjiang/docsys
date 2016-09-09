#encoding:utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from verify.models import Staff
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from email.mime.text import MIMEText
import re,md5,smtplib,base64,os,time

# 该文件主要作用是验证用户身份
#
#提供了用账户设置与身份验证接口
#
#@author Ivone
#@version 0.0.1

#登入页面
def index(request):
    return render(request,'verify/signin.html')

#忘记密码页面
def retrieve(request):
    return render(request,'verify/retrieve.html')

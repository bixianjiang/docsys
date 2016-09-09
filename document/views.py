#encoding:utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from document.models import Doc
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from email.mime.text import MIMEText
import re,md5,smtplib,base64,os,time

# 该文件主要作用是用户的文档编辑
#
#可以编辑以、分享、阅读文档
#
#@author Ivone
#@version 0.0.1

#列表页
def list(request):
    return render(request,'document/list.html')

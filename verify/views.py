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

#设置个人信息页面
def setIfo(request):
    return render(request,'verify/setInfo.html')

#登入动作
def signin(request):
    user = Staff.objects.get("email = %s"%(request.POST['email']))
    if user.password = md5.new(request.POST['pwd']).hexdigest():
        request.session['staff'] = user.id
        if user.status == 1:
            return HttpResponse(2)
        else:
            request.session['name'] = user.name
            return HttpResponse(1)
    else:
        return HttpResponse(0)

#忘记密码动作
def reset(request):
    user = Staff.objects.get("email = %s"%(request.POST['email']))
    if user:
        code = randomCode()
        title = "[GencONE文档系统] 重置密码"
        content = "我们于%s收到了您给我们提交的重置密码申请，如果不是您本人操作，请忽视该邮件。<br>您的安全验证码为:%s，请尽快输入验证码，确认身份后您可以重新设置您的密码。"
        result = sendEmail(request.POST['email'],title,content)
        if result :
            return HttpResponse("%s#%s"%(str(1),str(code)))
        else:
            return HttpResponse(2)
    else:
        return HttpResponse(0)

#新用户登入
def setStaffInfo(request):
    info = Staff.object(id = request.session['staff']).update(name = request.POST['name'], password = md5.new(request.POST['pwd']).hexdigest(), status = 2)
    if info:
        return HttpResponseRedirect(reverse('document:list'))
    else:
        return HttpResponseRedirect(reverse('verify:setIfo'))

#生成随机码
def randomCode():
    str = ''
    chars = 'abcdefghigklmnopqrstuvwxyz0123456789'
    length = 7
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

#发送邮件
def sendEmail(address,title,content):
    mailHost = "smtp.exmail.qq.com"
    mailUser = "service@gencone.com"
    mailPass = "GencONE2016"
    me = "service@gencone.com"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = address
    msg['From'] = me
    msg['To'] = address
    try:
        server = smtplib.SMTP()
        server.connect(mailHost)
        server.login(mailUser,mailPass)
        server.sendmail(me, address, content.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

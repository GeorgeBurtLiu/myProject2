from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import Student


def index_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if uname and pwd:
            student = Student(sname=uname, spwd=pwd)
            student.save()
            return HttpResponse('注册成功！')
    return HttpResponse('注册失败！')

from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext

from .models import User




def login(request):
    return render(request, 'myApp/page-login.html')


def index(request):
    return render(request, 'myApp/index.html')


def authenticate(request):
    userList = User.objects.all()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip() #去除首尾空格
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = User.objects.get(uname=username)
                if user.upassword == password:
                    return render(request, 'myApp/index.html')
                    #return redirect('myApp/index.html') #这个方法可以进入Index页面，但是没有css样式
                else:
                    message = "用户名或者密码不正确！"
            except:
                message = "用户名或者密码不正确！"
                return render(request, 'myApp/page-login.html', {"message": message})
        else:
            message = "请输入用户名和密码！"
        return render(request, 'myApp/page-login.html', {"message": message})
    return render(request, 'myApp/page-login.html')




def tables(request):
    return render(request, 'myApp/tables.html')

def draw(request):
    return render(request, 'myApp/draw.html')

def detail(request, num, num2):
    return HttpResponse("detail-%s-%s" % (num, num2))

# from .models import Grades,Students
# def grades(request):
#     # 去模板里取数据
#     gradesList = Grades.objects.all()
#     #将数据传递给模板，模板渲染页面，将渲染好的页面返回给浏览器
#     return render(request, 'myApp/grades.html', {"grades":gradesList})
#
# def students(request):
#     studentsList = Students.objects.all()
#     return render(request, 'myApp/students.html', {"students":studentsList})
#
# def gradesStudents(request, num):
#     grade = Grades.objects.get(pk=num)
#     studentsList = grade.students_set.all()
#     return render(request, 'myApp/students.html', {"students":studentsList})

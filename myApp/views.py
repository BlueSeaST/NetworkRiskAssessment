from django.shortcuts import render, redirect

from .models import User


# Create your views here.


def login(request):
    # 如果用户已经登录，直接跳转到主界面
    username = request.session.get('username', None)
    if username:
        # return render(request, 'myApp/index.html', {"username":username}) # 可以进入Index页面，有css样式，但是网页地址不变
        return redirect('index.html')

    # 如果未登录，用login的信息验证登录
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            username = username.strip()  # 去除首尾空格
            # 用户名和密码验证
            try:
                user = User.objects.get(uname=username)
                if user.upassword == password:
                    # 登录成功后将用户信息保存到session中，session的过期时间在setting.py里设置
                    request.session['username'] = username
                    return redirect('index.html')  # 没有传过来username值，Index页面可以通过session获取
                else:
                    message = "用户名或者密码不正确！"
            except:
                message = "用户名或者密码不正确！"
        else:
            message = "请输入用户名和密码！"
        return render(request, 'myApp/page-login.html', {"message": message})
    return render(request, 'myApp/page-login.html')
    # return redirect('login.html')  # 重定向改变网址，调用url分发器，再调用views中的函数，如果重定向到自身，会死循环


def index(request):
    # 判断用户是否已经登录，如果没有登录的话，跳转到login
    username = request.session.get('username', None)
    if not username:
        return redirect('login.html')  # 重定向改变网页

    return render(request, 'myApp/index.html', {"username": username})


def profile(request):
    username = request.session.get('username', None)
    if not username:
        # return render(request, 'myApp/page-login.html') # 这个不改变网页地址，不好
        return redirect('login.html')  # 重定向改变网页

    return render(request, 'myApp/page-profile.html', {"username": username})


def logout(request):
    username = request.session.get('username', None)
    if not username:
        # return render(request, 'myApp/page-login.html') # 这个不改变网页地址，不好
        return redirect('login.html')  # 重定向改变网页

    # 将用户信息从session里除去
    del request.session['username']
    return redirect('login.html')


def draw(request):
    username = request.session.get('username', None)
    if not username:
        # return render(request, 'myApp/page-login.html') # 这个不改变网页地址，不好
        return redirect('login.html')  # 重定向改变网页

    return render(request, 'myApp/draw.html', {"username": username})


# def gradesStudents(request, num):
#     grade = Grades.objects.get(pk=num)
#     studentsList = grade.students_set.all()
#     return render(request, 'myApp/students.html', {"students":studentsList})

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.views import View
# Create your views here.


class Login_View(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username, password = request.POST.get('userName'), request.POST.get('passWord')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/user/index')
        else:
            return render(request, 'login.html', {'err': '用户名或密码错误'})





def index_page(request):
    if not request.user.username:
        return redirect('/user/login')
    else:
        return render(request, 'main.html')
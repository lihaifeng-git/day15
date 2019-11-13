from django.shortcuts import render,redirect,reverse
from app01 import models
from django.views import View
from functools import wraps
from django.utils.decorators import method_decorator
import time
# Create your views here.
def timer(func):
    @wraps(func)
    def inner(*args,**kwargs):
        start=time.time()
        ret=func(*args,**kwargs)
        print('{}运行用了{}ms'.format(func.__name__,int(((time.time()-start))*1000)))
        return ret
    return inner
def index(request):
    name = request.GET.get('name')
    if name and models.User.objects.filter(username=name):
        return render(request,'index.html',{'name':name})
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        user=request.POST.get('user')
        passwd=request.POST.get('password')
        if models.User.objects.filter(username=user,password=passwd):
            return redirect('/app01/index/?name='+user)
        elif user=='' or passwd=='':
            return render(request,'login.html',{'error':'用户名或密码不能为空'})
        return render(request,'login.html',{'error':'用户名或密码错误'})
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        passwd = request.POST.get('password')
        if models.User.objects.filter(username=user):
            return  render(request,'register.html',{'error':'用户名已存在'})
        elif not user:
            return render(request, 'register.html', {'error': '用户名不能为空'})
        models.User.objects.create(username=user,password=passwd)
        return redirect('/app01/login/')

    return render(request,'register.html')

def publisher_list(request):
    all_publishers = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'all_publishers': all_publishers})
@method_decorator(timer,name='dispatch')
class Publishadd(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'publisher_add.html')
    def post(self,request,*args,**kwargs):
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(request, 'publisher_add.html', {'error': '名称不能为空'})
        models.Publisher.objects.create(name=pub_name)
        return redirect(reverse('app01:pub'))
# def publisher_add(request):
#     if request.method == 'POST':
#         pub_name = request.POST.get('pub_name')
#         if not pub_name:
#             return render(request, 'publisher_add.html', {'error': '名称不能为空'})
#         ret = models.Publisher.objects.create(name=pub_name)
#         print(ret, type(ret))
#         return redirect(reverse('app01:pub'))
#     return render(request, 'publisher_add.html')


def publisher_del(request,pk):
    # pk = request.GET.get('pk')
    # models.Publisher.objects.get(pk=pk).delete()
    models.Publisher.objects.filter(pk=pk).delete()
    return redirect(reverse('app01:pub'))


def publisher_edit(request,pk):
    # pk = request.GET.get('pk')
    obj = models.Publisher.objects.get(pk=pk)
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        obj.name = pub_name
        obj.save()
        return redirect(reverse('app01:pub'))
    return render(request, 'publisher_edit.html', {'obj': obj})
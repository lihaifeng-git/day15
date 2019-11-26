from django.shortcuts import render,redirect,reverse
from app01 import models
from django.views import View
from functools import wraps
from django.utils.decorators import method_decorator
import time
# Create your views here.
def login_require(func):
    def inner(request,*args,**kwargs):
        is_login=request.COOKIES.get('is_login')
        if is_login != '1':
            url=request.path_info
            return redirect('{}?return={}'.format(reverse('login'),url))
        ret=func(request,*args,**kwargs)
        return ret
    return inner
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
            returnurl=request.GET.get('return')
            if returnurl:
                response=redirect(returnurl)
            else:
                response=redirect(reverse('publisher'))
            response.set_cookie('is_login','1')
            # return redirect('/app01/index/?name='+user)
            return response
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
        return redirect(reverse('login'))
    return render(request,'register.html')
@login_require
def publisher_list(request):
    all_publishers = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'all_publishers': all_publishers})
@method_decorator(login_require,name='dispatch')
@method_decorator(timer,name='dispatch')
class Publishadd(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'publisher_add.html')
    def post(self,request,*args,**kwargs):
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(request, 'publisher_add.html', {'error': '名称不能为空'})
        models.Publisher.objects.create(name=pub_name)
        return redirect(reverse('publisher'))
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
    return redirect(reverse('publisher'))


def publisher_edit(request,pk):
    # pk = request.GET.get('pk')
    obj = models.Publisher.objects.get(pk=pk)
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        obj.name = pub_name
        obj.save()
        return redirect(reverse('publisher'))
    return render(request, 'publisher_edit.html', {'obj': obj})
@login_require
def book_list(request):
    all_book=models.Book.objects.all()
    return render(request,'book.html',{'all_book':all_book})
@method_decorator(login_require,name='dispatch')
class BookAdd(View):
    def get(self,request):
        all_publishers = models.Publisher.objects.all()
        return render(request,'book_add.html',{'all_publishers':all_publishers})
    def post(self,request):
        title=request.POST.get('book_name')
        pub=request.POST.get('pub_name')
        if not title:
            return render(request,'book_add.html',{'error':'名称不能为空'})
        models.Book.objects.create(title=title,pub_id=pub)
        return redirect(reverse('book'))

class BookEdit(View):
    def get(self,request,pk):
        all_publishers = models.Publisher.objects.all()
        book_obj=models.Book.objects.get(pk=pk)
        return render(request,'book_edit.html',{'all_publishers':all_publishers,'book_obj':book_obj})
    def post(self,request,pk):
        all_publishers = models.Publisher.objects.all()
        book_obj = models.Book.objects.get(pk=pk)
        title=request.POST.get('book_name')
        pub=request.POST.get('pub_name')
        if not title:
            return render(request,'book_edit.html',{'error':'名称不能为空','all_publishers':all_publishers,'book_obj':book_obj})
        models.Book.objects.filter(pk=pk).update(title=title,pub_id=pub)
        return redirect(reverse('book'))

def delete(request,table,pk):
    obj=getattr(models,table.capitalize())
    obj.objects.get(pk=pk).delete()
    return redirect(reverse(table))
@login_require
def author_list(request):
    all_authors=models.Author.objects.all()
    return render(request,'author.html',{'all_authors':all_authors})
@login_require
def author_add(request):
    all_books=models.Book.objects.all()
    if request.method == 'POST':
        author_name=request.POST.get('author_name')
        if not author_name:
            return render(request, 'author_add.html',{'error':'作者名字不能为空','all_books':all_books})
        book_name=request.POST.getlist('book_name')
        author_obj=models.Author.objects.create(name=author_name)
        author_obj.books.set(book_name)
        return redirect(reverse('author'))
    return render(request,'author_add.html',{'all_books':all_books})

def author_edit(request,pk):
    all_books = models.Book.objects.all()
    author_obj=models.Author.objects.get(pk=pk)
    if request.method == 'POST':
        author_name=request.POST.get('author_name')
        if not author_name:
            return render(request,'author_edit.html',{'all_books':all_books,'author_obj':author_obj,'error':'作者名字不能为空'})
        book_name=request.POST.getlist('book_name')
        author_obj.name=author_name
        author_obj.save()
        author_obj.books.set(book_name)
        return redirect(reverse('author'))
    return render(request,'author_edit.html',{'all_books':all_books,'author_obj':author_obj})
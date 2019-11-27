from django.shortcuts import render,HttpResponse

# Create your views here.

def re(request):
    if request.method=='POST':
        i1=request.POST.get('i1')
        i2=request.POST.get('i2')
        i3=int(i1)+int(i2)
        # return render(request, 're.html',{'i1':i1,'i2':i2,'i3':i3})
        return HttpResponse(i3)
    return render(request,'re.html')

def file_upload(request):
    if request.method=='POST':
        f1=request.FILES.get('f1')
        with open(f1.name,'wb') as f:
            for i in f1.chunks():
                f.write(i)
    return render(request,'file_upload.html')
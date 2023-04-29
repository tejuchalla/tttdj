from django.shortcuts import render
from pa.models import Acc
from pa.forms import Myform
# Create your views here.
def home(req):
    return render(req,'index.html')
def f(req):
    form = Myform
    pf={'form':form}
    if req.method=='POST':
        form = Myform(req.POST)
        if form.is_valid():
            form.save()
        return home(req)

    return render(req,'f.html',pf)
def a(req):
    result=Acc.objects.all()
    td={"alla":result}
    return render(req,'A.html',td)

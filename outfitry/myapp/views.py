
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def signup(request):
    return render(request, 'myapp/signup.html')

def login_view(request):
    return render(request, 'myapp/login.html')

def matching_view(request):
    return render(request, 'myapp/matching.html')

def community(request):
    return render(request, 'myapp/community.html')

def content(request):
    return render(request, 'myapp/content.html')

def company(request):
    return render(request, 'myapp/company.html')

def custom(request):
    return render(request, 'myapp/custom.html')

def price(request):
    return render(request, 'myapp/price.html')

def shopdetail1(request):
    return render(request, 'myapp/shop-detail1.html')

def shopdetail2(request):
    return render(request, 'myapp/shop-detail2.html')

def shopdetail3(request):
    return render(request, 'myapp/shop-detail3.html')

def shopdetail4(request):
    return render(request, 'myapp/shop-detail4.html')

def fashionista(request):
    return render(request, 'myapp/fashionista.html')

def supernova(request):
    return render(request, 'myapp/supernova.html')

def poweroutfit(request):
    return render(request, 'content/poweroutfit.html')

def colortone(request):
    return render(request, 'content/colortone.html')

def gogreener(request):
    return render(request, 'content/gogreener.html')

def diy(request):
    return render(request, 'content/diy.html')


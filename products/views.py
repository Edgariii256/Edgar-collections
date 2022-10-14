from django.shortcuts import render

# Create your views here.
def index_3(request):
    return render(request,'index-3.html')

def index_1(request): 
    
    return render(request,'index-1.html')


def index_2(request):
    return render(request,'index-2.html') 


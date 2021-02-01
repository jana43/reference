from django.shortcuts import render
from django.http import HttpResponse
from .models import Post , category
# Create your views here.


def index(request):
    data = Post.objects.all()
    lessons = category.objects.all()

    return render(request , 'index.html' , {'data':data,'lessons':lessons})


def get_page(request , slug_text):
    page = category.objects.filter(slug = slug_text)
    if page.exists():
        page = page.first()
        data = Post.objects.filter(category = page.tittle)
    else:
        return HttpResponse("page not found")

    return render(request , 'page.html' ,{'data':data})

def show(request , slug_text):
    data = Post.objects.filter(slug = slug_text)
    if data.exists():
        data = data.first()
    else:
        return HttpResponse("page not found")
    
    return render(request , 'show.html',{'data':data})


def search(request):
    if request.method == "POST":
        text = request.POST.get("text")
        print(">>>>>>>>>>>>>>>>",text)
        search_data = []
        data_base_fetch = Post.objects.all()
        text = text.split()
        i = 0
        for item in data_base_fetch:           
            for word in text:
                if word.lower() in item.data.lower() + item.tittle.lower() + item.category.lower():
                    i = i+1
            if len(text) == i:
                search_data.append(item)
        print(">>>>>>>>>>>>>>>>>>>>>",search_data)
        return render(request,'search.html'  , {'data':search_data})
    else:
        return render(request , 'index.html')
        
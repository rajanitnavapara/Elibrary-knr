from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def books(request):
    lists = {'list1' : [1,2,3,4,5,6,7,5,9]
    }
    return render(request,'ebook_list.html',lists)


def about(request):
    return render(request,'about.html')       
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from  django.contrib import messages
from .models import New_post

# Create your views here.


def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def category(request):
    return render(request,'catagory.html')

def category_post(request):
    return render(request,'catagory-post.html')

def recipe(request):
    return render(request,'all_recipe.html')

def single_post(request):
    return render(request,'single_post.html')

def recipe1(request):
    return render(request,'chicken biryani.html')

def recipe2(request):
    return render(request,'veg salad.html')

def recipe3(request):
    return render(request,'ramen.html')

def recipe4(request):
    return render(request,'gravy.html')

def recipe5(request):
    return render(request,'momos.html')

def recipe6(request):
    return render(request,'soup.html')

def recipe7(request):
    return render(request,'fruit salad.html')

def recipe8(request):
    return render(request,'samosa.html')

def recipe9(request):
    return render(request,'vegan spinach.html')

def recipe10(request):
    return render(request,'pasta.html')

def category1(request):
    return render(request,'category_file/cat1.html')

def category2(request):
    return render(request,'category_file/cat2.html')

def category3(request):
    return render(request,'category_file/cat3.html')

def category4(request):
    return render(request,'category_file/cat4.html')

def category5(request):
    return render(request,'category_file/cat5.html')

def category6(request):
    return render(request,'category_file/cat6.html')

def category7(request):
    return render(request,'category_file/cat7.html')

def category8(request):
    return render(request,'category_file/cat8.html')

def category9(request):
    return render(request,'category_file/cat9.html')

def main_post1(request):
    return render(request,'category_file/biryani_main1.html')

def main_post2(request):
    return render(request,'category_file/biryani_main2.html')





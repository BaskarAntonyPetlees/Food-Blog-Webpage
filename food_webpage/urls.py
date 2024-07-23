from django.urls import path
from . import views

urlpatterns = [
    
    # url request for home/index page
    path('',views.index,name='index'),
    
    # url request for contact us page
    path('contact',views.contact,name='contact'),
    
    # url request for about us page
    path('about',views.about,name='about'),
    
    # url request for category_home page
    path('category',views.category,name='category'),

    # url request for overall_recipe page
    path('recipe',views.recipe,name='recipe'),
   
    # url request for recipe pages
    path('recipe1',views.recipe1,name='recipe1'),
    path('recipe2',views.recipe2,name='recipe2'),
    path('recipe3',views.recipe3,name='recipe3'),
    path('recipe4',views.recipe4,name='recipe4'),
    path('recipe5',views.recipe5,name='recipe5'),
    path('recipe6',views.recipe6,name='recipe6'),
    path('recipe7',views.recipe7,name='recipe7'),
    path('recipe8',views.recipe8,name='recipe8'),
    path('recipe9',views.recipe9,name='recipe9'),
    path('recipe10',views.recipe10,name='recipe10'),
    
    # url request for category pages
    path('category1',views.category1,name='category1'),
    path('category2',views.category2,name='category2'),
    path('category3',views.category3,name='category3'),
    path('category4',views.category4,name='category4'),
    path('category5',views.category5,name='category5'),
    path('category6',views.category6,name='category6'),
    path('category7',views.category7,name='category7'),
    path('category8',views.category8,name='category8'),
    path('category9',views.category9,name='category9'),
    
    # url request for main post
    path('main_post1',views.main_post1,name='main_post1'),
    path('main_post2',views.main_post2,name='main_post2'),

]

"""myfirstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  main.views import main, test, test1, test2, test3, main1, hoby, skills, sport, books 
# from  test.views import main
# from  test1.views import main
# from  test2.views import main
# from  test3.views import main
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main', main, name='main'),
    path('test', test, name='test'),
    path('test1', test1, name='test1'),
    path('test2', test2, name='test2'),
    path('test3', test3, name='test3'),
    path('', main1, name='main1'),
    path('hoby', hoby, name='hoby'),
    path('skills', skills, name='skills'),
    path('sport', sport, name='sport'),
    path('books', books, name='books')
]

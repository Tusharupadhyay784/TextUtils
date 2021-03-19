"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views # for importing view here we should do this
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'), # first it django goes in path folder then it sees there is some views here so it goes in views folder and whatever in views folder it throws in the browser
    # path('removepunc',views.removepunc,name="removepunc"),
    path('analyze',views.Analyze,name="analyze")
    

    
    
    
]













































































# path('about',views.about,name="about"), 
    # path('removepunc',views.removepunc,name='rempunc'),
    # path('capital',views.capfirst,name='capfirst'),
    # path('new',views.newlineremove,name='newlineremove'),
    # path('space',views.spaceremove,name='spaceremove'),
    # path('char',views.charcount,name='charcount'),
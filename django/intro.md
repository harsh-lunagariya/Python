*Django is a high-level Python web framework that makes it easier and faster to build web applications.

-Django follows the Model–View–Template (MVT) pattern, similar to MVC.

-majority component available for development

-provide security

-scalability

-That use in rapid applications development

    
*create virtual environment with
-uv venv

*To install Django use
-uv pip install Django

*To Start project use
-django-admin startproject <project_name>
-cd <project_name>


*For run server use
-python manage.py runserver <port_number>"default is 8000"
-also note that you are in project directory


* HTML page adding
-for httpreponse from django.http import Httpreponse
-return Httpreponse('msg')
-for rendering file use from django.shortcuts import render
-then return render(request, 'filepath')
-then in setting.py add the templates directory in TEMPLATES -> DIRS add in list


* CSS loading 
-in html page for link css in href use {% static 'style.css' %}
-also top of the page load static {% load static %}
-then change settings for that in settings.py import os
-add after STATIC_URL add STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]


*Creating app
-python3 manage.py startapp <app_name>
-add the file name in setting.py in INSTALLED_APPS
-create templates/<app_name> folder in app , this no need to configure
-create or put html file in this folder
-in project urls.py add path like below and also import include from django.urls
    path('<app_name>/', include(<app_name>.urls))
-also create a file in app urls.py

*Creating layout page that all can use it
-in our root template dir create layout.html and write layout and block name
-that layout we can extend in any of our file 


*with Tailwind css
-uv pip install django-tailwind
-pip install 'django-tailwind[reload]'
-add app in settings 'tailwind'
-run command $python3 manage.py tailwind init
-add app in setting or default 'theme'
-in setting create TAILWIND_APP_NAME = 'theme' 
- same creat INTERNAL_IPS = ['127.0.0.1']
-run command $python3 manage.py tailwind install
-run command for production ready $python3 manage.py tailwind build
-run command in diffrent terminal for start tailwind $python3 manage.py tailwind start
-for auto reload follow below step 
-add this into INSTALLED_APPS 'django_browser_reload',
-add this into MIDDLEWARE 'django_browser_reload.middleware.BrowserReloadMiddleware',
-add this in urls path("__reload__/",include("django_browser_reload.urls")),
-restart all terminal

*Admin pannel
-python3 manage.py migrate
-python3 manage.py createsuperuser


*image setting.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
-in root urls.py
from django.conf import settings
from django.conf.urls.static import static
-urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
python3 manage.py makemigrations <app_name>
python3 manage.py migrate

*model of app that add in admin
from .models import <modelname>
admin.site.register(modelname)


**after performing model operation must do makemigrations and then migrate


* Writing models.py
from django.db import models
class modelname(models.Model):
    ...
    def __str__(self):
        return self.name  ->this name is name that you want to show in admin pannel
-add that in admin.py
from .models import modelname
class modeladmin(admin.ModelAdmin):
    list_display = ()   -> makesure that is in tuple
admin.site.register(modelname, modeladmin)


    
"""startdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from Home_App import views as hv
from startdjango import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', hv.home, name='Home'),
                  path('about/', hv.about, name='About'),
                  path('book_table/', hv.book_table, name='Book_Table'),
                  path("feadback/", hv.feedback, name="Feedback_Form"),
                  path('menu/', hv.menu, name='Menu'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_URL) + static(settings.MEDIA_URL,
                                                                                          document_root=settings.MEDIA_URL)

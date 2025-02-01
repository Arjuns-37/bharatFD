# # myproject/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),  # Admin page
#     path('api/', include('faq.urls')),  # Include the FAQ app's URLs
# ]


from django.contrib import admin
from django.urls import path, include
from faq import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('faq.urls')),
      path('', views.home, name='home'),  
     
]



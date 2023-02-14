"""honeyrae URL Configuration

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

# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from repairsapi.views import register_user, login_user
from rest_framework import routers
from repairsapi.views import CustomerView
from repairsapi.views import TicketView
from repairsapi.views import EmployeeView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')
router.register(r'tickets', TicketView, 'ticket')
router.register(r'employees', EmployeeView, 'employee')



# The trailing_slash=False tells the router to accept /customers instead of /customers/. It’s a very annoying error to come across, when your server is not responding and the code looks right, the only issue is your fetch url is missing a / at the end.

# The next line is what sets up the /customers resource. The first parameter, r'customers, is setting up the URL. The second CustomerView is telling the server which view to use when it sees that url.

# The third, customer, is called the base name. You’ll only see the base name if you get an error in the server. It acts as a nickname for the resource and is usually the singular version of the URL.


urlpatterns = [
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from repairsapi.views import register_user, login_user, EmployeeView, CustomerView, TicketView
from rest_framework import routers


# set the router variable

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')
router.register(r'employees', EmployeeView, 'employee')
router.register(r'tickets', TicketView, 'ticket')

# The first parameter, r'customers, is setting up the URL.
# The second CustomerView is telling the server which view to use when it sees that url.
# The third, customer, is called the base name

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

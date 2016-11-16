from django.conf.urls import url,include
from rest_framework import routers


from . import views

# router = routers.DefaultRouter()
# router.register(r'users',views.all_tickets_collection)
# router.register(r'groups',views.GroupViewSet)


urlpatterns = [
    #url(r'^',include(router.urls)),
    #url(r'^$', views.index, name='index'),
    url(r'^',views.all_tickets_collection, name='all_tickets_collection'),
    ]


from django.conf.urls import url, include
from sign import views_if

urlpatterns = [
    url(r'^api/', include('sign.urls', namespace="sign")),
    # sign system interface
    # ex : /api/add_event/
    url(r'^add_event/', views_if.add_event, name='add_event'),
]
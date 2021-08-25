from django.conf.urls import url

from app_expect.views import List_elec_View, ELEC_Base_View

urlpatterns = [
    url('list/', List_elec_View.as_view(), name="list"),
    url('elec/', ELEC_Base_View.as_view(), name="elec"),
]
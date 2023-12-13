from django.urls import path

from . import views

app_name = "party"

list_parties_urlpatterns = [
    path("", views.PartyListPage.as_view(), name="page_party_list"),
]

urlpatterns = list_parties_urlpatterns

from django.urls import path

from . import views

app_name = "party"

list_parties_urlpatterns = [
    path("", views.PartyListPage.as_view(), name="page_party_list"),
]

party_detail_urlpatterns = [
    path("<uuid:party_uuid>/", views.PartyDetailPage.as_view(), name="page_single_party"),
    path("<uuid:party_uuid>/details/", views.PartyDetailPartial.as_view(), name="partial_party_detail"),
]

new_party_urlpatterns = [
    path("new/", views.page_new_party, name="page_new_party"),
    path("new/check-date/", views.partial_check_party_date, name="partial_check_party_date"),
    path("new/check-invitation/", views.partial_check_invitation, name="partial_check_invitation"),
]

urlpatterns = list_parties_urlpatterns + party_detail_urlpatterns + new_party_urlpatterns

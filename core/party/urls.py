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

gift_registry_urlpatterns = [
    path("<uuid:party_uuid>/gifts/", views.GiftRegistryPage.as_view(), name="page_gift_registry"),
    path("gifts/<uuid:gift_uuid>/", views.GiftDetailPartial.as_view(), name="partial_gift_detail"),
    path("gifts/<uuid:gift_uuid>/form/", views.GiftUpdateFormPartial.as_view(), name="partial_gift_update"),
    path("gifts/<uuid:gift_uuid>/delete/", views.delete_gift_partial, name="partial_gift_delete"),
    path("<uuid:party_uuid>/new-gift/", views.GiftCreateFormPartial.as_view(), name="partial_new_gift"),
]

guest_list_urlpatterns = [
    path("<uuid:party_uuid>/guests/", views.GuestListPage.as_view(), name="page_guest_list"),
    path("<uuid:party_uuid>/guests/mark-attending/", views.mark_attending_partial, name="partial_mark_attending"),
    path(
        "<uuid:party_uuid>/guests/mark-not-attending/",
        views.mark_not_attending_partial,
        name="partial_mark_not_attending",
    ),
]


urlpatterns = (
    list_parties_urlpatterns
    + party_detail_urlpatterns
    + new_party_urlpatterns
    + gift_registry_urlpatterns
    + guest_list_urlpatterns
)

import pytest
from django.urls import reverse

from core.party.models import Party


@pytest.mark.django_db
def test_create_party(authenticated_client, create_user):
    url = reverse("party:page_new_party")
    data = {
        "party_date": "2025-06-06",
        "party_time": "18:00:00",
        "venue": "My Venue",
        "invitation": "Come to my party!",
    }

    response = authenticated_client(create_user).post(url, data)

    assert response.status_code == 302
    assert Party.objects.count() == 1


# NEW
def test_create_party_invitation_too_short_returns_error(
    authenticated_client,
    create_user,
):
    url = reverse("party:page_new_party")
    data = {
        "party_date": "2025-06-06",
        "party_time": "18:00:00",
        "venue": "My Venue",
        "invitation": "Too short",
    }

    response = authenticated_client(create_user).post(url, data)

    assert not response.context["form"].is_valid()
    assert "You really should write an invitation." in response.content.decode()
    assert Party.objects.count() == 0


# NEW
def test_create_party_past_date_returns_error(authenticated_client, create_user):
    url = reverse("party:page_new_party")

    data = {
        "party_date": "2020-06-06",
        "party_time": "18:00:00",
        "venue": "My Venue",
        "invitation": "Come to my party!",
    }

    response = authenticated_client(create_user).post(url, data)

    assert not response.context["form"].is_valid()
    assert "You chose a date in the past." in response.content.decode()
    assert Party.objects.count() == 0

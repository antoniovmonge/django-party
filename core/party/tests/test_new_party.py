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

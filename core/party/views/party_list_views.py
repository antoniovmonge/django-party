import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from core.party.models import Party


class PartyListPage(LoginRequiredMixin, ListView):
    template_name = "party/party_list/page_parties_list.html"
    context_object_name = "parties"
    paginate_by = 6

    def get_queryset(self):
        return Party.objects.filter(
            organizer=self.request.user,
            party_date__gte=datetime.date.today(),
        ).order_by("party_date")

    def get_template_names(self):
        if "hx-request" in self.request.headers:
            return ["party/party_list/partial_parties_list.html"]
        else:
            return ["party/party_list/page_parties_list.html"]

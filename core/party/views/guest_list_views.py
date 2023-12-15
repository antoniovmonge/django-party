from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import QueryDict
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from core.party.models import Guest


class GuestListPage(LoginRequiredMixin, ListView):
    model = Guest
    template_name = "party/guest_list/page_guest_list.html"
    context_object_name = "guests"

    def get_queryset(self):
        return Guest.objects.filter(party_id=self.kwargs["party_uuid"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["party_id"] = self.kwargs["party_uuid"]
        return context


@login_required
@require_http_methods(["PUT"])
def mark_attending_partial(request, party_uuid):
    mark_attending = QueryDict(request.body).getlist("guest_ids")
    Guest.objects.filter(uuid__in=mark_attending).update(attending=True)

    guests = Guest.objects.filter(party_id=party_uuid)

    return render(
        request,
        "party/guest_list/partial_guest_list.html",
        {"guests": guests},
    )


@login_required
@require_http_methods(["PUT"])
def mark_not_attending_partial(request, party_uuid):
    mark_not_attending = QueryDict(request.body).getlist("guest_ids")
    Guest.objects.filter(uuid__in=mark_not_attending).update(attending=False)

    guests = Guest.objects.filter(party_id=party_uuid)

    return render(
        request,
        "party/guest_list/partial_guest_list.html",
        {"guests": guests},
    )

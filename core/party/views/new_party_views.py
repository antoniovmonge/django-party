from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from core.party.forms import PartyForm


@login_required
def page_new_party(request):
    form = PartyForm()

    if request.method == "POST":
        form = PartyForm(request.POST)
        if form.is_valid():
            party = form.save(commit=False)
            party.organizer = request.user
            party.save()
            return redirect("party:page_single_party", party_uuid=party.uuid)

    return render(request, "party/new_party/page_new_party.html", {"form": form})

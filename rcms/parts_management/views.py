from django.shortcuts import render
from django.views.generic.edit import (CreateView, UpdateView,
                                       DeleteView, View)
from django.views.generic import ListView, UpdateView

from django.core.urlresolvers import reverse_lazy
from forms import PartsArrangementForm
from models import PartsArrangement
# Create your views here.


class PartCreateView(CreateView):
    """
    create vendor basic details
    """

    template_name = 'parts_management/part_create.html'
    form_class = PartsArrangementForm
    success_url = reverse_lazy('part_create')

    def form_valid(self, form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        form.save()
        form = PartsArrangementForm()
        msg = "successfully registered"
        return self.render_to_response(self.get_context_data(form=form,success=msg))


class PartListView(ListView):

    """
    Listing all data from consultant
    """

    model = PartsArrangement
    template_name = 'parts_management/part_list.html'
    context_object_name = 'part_list'
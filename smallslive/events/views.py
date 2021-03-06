from django.utils.timezone import datetime, timedelta
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin, UserPassesTestMixin

from .forms import EventAddForm
from .models import Event
from multimedia.models import Media


class HomepageView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        today = datetime.now().date()
        few_days_out = today + timedelta(days=3)
        context['events'] = Event.objects.filter(start_day__range=(today, few_days_out)).reverse()
        context['videos'] = Media.objects.order_by('-id')[:5]
        return context

homepage = HomepageView.as_view()


class EventAddView(CreateView):
    template_name = 'events/event_add.html'
    model = Event

event_add = EventAddView.as_view()


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/video.html'
    # def get_template_names(self):
    #     if self.object.is_past():
    #        template_name = 'events/video.html'
    #    else:
    #        template_name = 'events/event_detail.html'
    #    return [template_name]

event_detail = EventDetailView.as_view()

class EventEditView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventAddForm
    template_name = 'events/event_edit.html'

    # def test_func(self, user):
    #     """
    #     Show 403 forbidden page only when the logged in user doesn't have required
    #     permissions, redirect anonymous users to the login screen.
    #     """
    #     self.raise_exception = True
    #     try:
    #         artist_id_match = self.kwargs.get('pk') == str(user.artist.id)
    #     except Artist.DoesNotExist:
    #         artist_id_match = False
    #     return (artist_id_match or user.is_superuser)

event_edit = EventEditView.as_view()

class VenueDashboardView(ListView):
    queryset = Event.objects.order_by('-modified', '-start_day')[:50]
    template_name = 'dashboard-admin.html'
    context_object_name = 'events'

venue_dashboard = VenueDashboardView.as_view()


class MyGigsView(TemplateView):
    template_name = 'my_gigs.html'

    def get_context_data(self, **kwargs):
        context = super(MyGigsView, self).get_context_data(**kwargs)
        context['past_events'] = Event.past.filter(performers=self.request.user.artist)
        context['future_events'] = Event.upcoming.filter(performers=self.request.user.artist)
        return context

my_gigs = MyGigsView.as_view()

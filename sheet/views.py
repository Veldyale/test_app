from django.views.generic import ListView
from .models import *
from .google_in_python import import_google_sheet


class GoogleApi(ListView):
    model = Sheet
    template_name = 'sheet/index.html'
    context_object_name = 'sheet'

    def get_queryset(self):
        import_google_sheet()
        return Sheet.objects.all()

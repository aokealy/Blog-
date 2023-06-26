from django.views.generic import TemplateView

class CorePageView(TemplateView):
    template_name = 'blogapp/core.html'
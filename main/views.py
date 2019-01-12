from django.views.generic import TemplateView


class RootPageView(TemplateView):
    template_name = "main/root.html"

from django.views.generic.base import TemplateView

class RegistView(TemplateView):
    template_name = 'registration/regist.html'

class RegistDoneView(TemplateView):
    template_name = 'registration/regist_done.html'
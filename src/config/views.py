from django.shortcuts import render
from django.views.generic import TemplateView, View


class IndexView(TemplateView):
    template_name = 'index.html'


class AnotherView(View):

   def get(self, request):
       print("IP Address for debug-toolbar: " + request.META['HTTP_X_FORWARDED_FOR'])
       return render(request, 'another.html')


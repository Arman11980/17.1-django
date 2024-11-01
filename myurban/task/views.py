from django.shortcuts import render
from django.views.generic import TemplateView


def test(request):
    return render(request, 'second/func.html')


class ShabClass(TemplateView):
    template_name = 'second/class.html'
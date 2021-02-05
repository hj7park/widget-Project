from .models import Widget
from django.shortcuts import render
from .forms import widgetForm
from django.views.generic.edit import CreateView,DeleteView
# Create your views here.

def index(request):
    form = widgetForm()
    widgets = Widget.objects.all()
    total = 0
    for widget in widgets:
        total += widget.quantity
    context = {'form':form, 'widgets':widgets, 'total':total}
    return render(request, 'index.html', context)

class createWidget(CreateView):
    model = Widget
    form_class = widgetForm
    success_url ='/'

class deleteWidget(DeleteView):
    model = Widget
    success_url ='/'
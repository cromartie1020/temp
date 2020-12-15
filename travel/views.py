from django.shortcuts import render
from .forms import TravelForm
def travel_views(request):
    return render(request,'travel/travel.html',{})

def travel_form(request):
    form=TravelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form=TravelForm()

    return render(request, 'travel/form.html',{'form':form })    

    
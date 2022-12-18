from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status 
from .serializers import DispenseSerializer
from .forms import DispenseForm
import datetime
from .models import Dispense

# Create your views here.
def home (request):
    form = DispenseForm

    if request.method == 'POST':
        form = DispenseForm(request.POST)

        # dispensing_time

        splitted = request.POST['dispensing_time'].split(' ')
        splitted1 = splitted[4].split(':')
        # print(splitted1)
        dispensing_time = datetime.time(int(splitted1[0]), int(splitted1[1]), int(splitted1[2]))
        # print(type(dispensing_time), dispensing_time)

        # stop_dispensing_time

        splitted2 = request.POST['stop_dispensing_time'].split(' ')
        splitted3 = splitted2[4].split(':')
        # print(splitted3)
        stop_dispensing_time = datetime.time(int(splitted3[0]), int(splitted3[1]), int(splitted3[2]))
        # print(type(stop_dispensing_time), stop_dispensing_time)

        productname = request.POST['productname']

        dispensing_status = "open"

        # counting the price with assumption that ever


        new = Dispense(productname=productname, dispensing_status=dispensing_status, dispensing_time=dispensing_time, stop_dispensing_time=stop_dispensing_time)
        new.save()       

        # dispensing_time = datetime(request.POST['dispensing_time'])
        # print(dispensing_time)

    else:
        dispensing_status = "close"


            
    context = {'form': form}
    return render (request , 'index.html', context)

class DispenseList(APIView):
    def get (self, request):
        dispenses = Dispense.objects.all()
        serializer = DispenseSerializer(dispenses, many=True)
    
        return Response(serializer.data)
    





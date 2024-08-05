from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from demo.models import country,blog
# Create your views here.
obj= country.objects.all()
dep =blog.objects.all()
def submit(request):
    print(request.method)
    val = request.POST.get('val')
    print('************************--',val,'**************************')
    return HttpResponse(val)
    
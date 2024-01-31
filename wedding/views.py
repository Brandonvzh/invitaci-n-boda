from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.template import loader
from . import forms, models

import random

# Create your views here.
def random_code():
    '''
    
    '''
    length_code = 5
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = ''.join(random.choices(sample, k = length_code))
    return str(code)


def bride_form_view(request):
    '''
    
    '''
    if request.method == "GET":
        form = forms.Guests_bride_form() 
    if request.method == "POST":
        form = forms.Guests_bride_form(request.POST)
        if form.is_valid():
            form_instance = form.save()
            form_pk = form_instance.pk
            models.Guests.objects.filter(id = form_pk).update(code = random_code())
            
    return render(request = request, template_name = 'bride_form_template.html', context = {'form':form})


def wedding_invitation_view(request):
    if request.method == "POST":
        id = request.POST.get('id', None)
        asistentes = request.POST.get('asistentes', None)
        invitados = request.POST.get('invitados', None)
        asistencia = request.POST.get('asistencia', None)
        
        instancia = models.Guests.objects.get(id = int(id))
        
        if instancia:
            instancia.num_guests_selected = int(invitados)
            instancia.guests_names = str(asistentes)
            instancia.answer = str(asistencia)
            
            instancia.save()
        

    return render(request = request, template_name = 'wedding_invitation_template.html')


def guests_table(request):
    if request.method == "GET":
        guests_query = models.Guests.objects.all()
    return render(request, "guests_table.html", {'guests': guests_query})


def update_data(request, pk):
    '''
    
    '''
    if request.method == "POST":
        instance = models.Guests.objects.get(id = pk)
        form = forms.Guests_form(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return redirect('wedding_invitation_view')


def copy_data(request):
    if request.method == "GET":
        query = models.Guests.objects.all()
        print(query[0].num_guests_selected_char)
    return render(request, "x.html", {})
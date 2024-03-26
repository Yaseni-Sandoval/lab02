from django.shortcuts import render
import math
# Create your views here.

def calculavol(request):
    volumen = None
    if request.method == 'POST':
        altura = float(request.POST.get('altura'))
        diametro = float(request.POST.get('diametro'))
        radio = diametro / 2
        volumen = math.pi * radio**2 * altura
        contexto = {
            'altura': altura,
            'diametro': diametro,
            'volumen': volumen,
        }
    else:
        contexto = {}
    return render(request, 'calculavol/calculavol.html', contexto)
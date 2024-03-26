from django.shortcuts import render

def calculo(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        operacion = request.POST.get('operacion')
        resultado = None
        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        contexto = {
            'num1': num1,
            'num2': num2,
            'operacion': operacion,
            'resultado': resultado
        }
        return render(request, 'calculo/resultado.html', contexto)
    return render(request, 'calculo/calculo.html')
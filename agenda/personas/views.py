from django.shortcuts import render, redirect, get_object_or_404

from .models import Persona, Ciudad


def lista_personas(request):
	personas = Persona.objects.all()
	return render(request, 'personas/lista_personas.html', {'personas': personas})


def crear_persona(request):
	ciudades = Ciudad.objects.all()
	if request.method == 'POST':
		documento = request.POST['documento']
		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		direccion = request.POST['direccion']
		correo = request.POST['correo']
		ciudad_id = request.POST['ciudad']
		ciudad = Ciudad.objects.get(id=ciudad_id)

		Persona.objects.create(
			documento=documento,
			nombre=nombre,
			apellido=apellido,
			direccion=direccion,
			correo=correo,
			ciudad=ciudad,
		)
		return redirect('lista_personas')

	return render(request, 'personas/form_persona.html', {'ciudades': ciudades})


def editar_persona(request, id):
	persona = get_object_or_404(Persona, id=id)
	ciudades = Ciudad.objects.all()
	if request.method == 'POST':
		persona.documento = request.POST['documento']
		persona.nombre = request.POST['nombre']
		persona.apellido = request.POST['apellido']
		persona.direccion = request.POST['direccion']
		persona.correo = request.POST['correo']
		persona.ciudad = Ciudad.objects.get(id=request.POST['ciudad'])
		persona.save()
		return redirect('lista_personas')

	return render(
		request,
		'personas/form_persona.html',
		{'persona': persona, 'ciudades': ciudades},
	)


def eliminar_persona(request, id):
	persona = get_object_or_404(Persona, id=id)
	if request.method == 'POST':
		persona.delete()
		return redirect('lista_personas')

	return render(request, 'personas/eliminar_persona.html', {'persona': persona})

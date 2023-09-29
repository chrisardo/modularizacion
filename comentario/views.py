from django.shortcuts import render
from django.http import HttpResponse
from .models import Coment


# Create your views here.
def test(request):
    return HttpResponse("Hola mundo")


def create(request):
    """
    comment = Coment(
        nombre="Juan",
        score=4,
        comment="Comentario de prueba",
        date="2021-10-10",
        signature="Firma",
    )
    comment.save()  # Guarda el objeto en la base de datos
    """
    comment = Coment.objects.create(
        nombre="Chrisardo",
        score=2,
        comment="Comentario de prueba2",
        date="2021-10-10",
        signature="Firma2",
    )  # Crea el objeto y lo guarda en la base de datos de forma directa
    return HttpResponse("Ruta para probar la creacion de los modelos")


def delete(request):
    """
    comment = Coment.objects.get(id=2)  # Obtiene el objeto de la base de datos
    comment.delete()  # Elimina el objeto de la base de datos
    """
    Coment.objects.filter(
        nombre="Chrisardo"
    ).delete()  # Elimina el objeto de la base de datos de forma directa
    return HttpResponse("Ruta para probar la eliminacion de los modelos")

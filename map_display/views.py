from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.shortcuts import render
from .models import *


def electric_poles_map(request):
    electric_poles = ElectricPole.objects.all()
    electric_pole_connections = ElectricPoleConnection.objects.all()
    connections = []

    for connection in electric_pole_connections:
        connection_line = [
            [connection.pole_from.location.y, connection.pole_from.location.x],
            [connection.pole_to.location.y, connection.pole_to.location.x]
        ]
        connections.append(connection_line)

    return render(request, 'pole_map.html', {'electric_poles': electric_poles, 'connections': connections})


def get_connected_poles(request):
    pole_id = request.GET.get('pole_id')
    connections_from = ElectricPoleConnection.objects.filter(pole_from_id=pole_id)
    connections_to = ElectricPoleConnection.objects.filter(pole_to_id=pole_id)
    
    connected_poles_from = [{
        'id': connection.pole_to.id,
        'pole_ID': connection.pole_to.pole_ID,
        'location': {
            'x': connection.pole_to.location.x,
            'y': connection.pole_to.location.y
        }
    } for connection in connections_from]

    connected_poles_to = [{
        'id': connection.pole_from.id,
        'pole_ID': connection.pole_from.pole_ID,
        'location': {
            'x': connection.pole_from.location.x,
            'y': connection.pole_from.location.y
        }
    } for connection in connections_to]

    return JsonResponse({'connected_poles_from': connected_poles_from, 'connected_poles_to': connected_poles_to}, safe=False)

from django.core.management import BaseCommand

from xyinc.api.models import Poi

_POIS = [{'name': 'Lanchonete', 'x': 27, 'y': 12},
         {'name': 'Posto', 'x': 31, 'y': 18},
         {'name': 'Joalheria', 'x': 15, 'y': 12},
         {'name': 'Floricultura', 'x': 19, 'y': 21},
         {'name': 'Pub', 'x': 12, 'y': 8},
         {'name': 'Supermercado', 'x': 23, 'y': 6},
         {'name': 'Churrascaria', 'x': 28, 'y': 2},
         ]


def _destroy_data():
    for p in Poi.get():
        p.delete()


def _init_data():

    for p in _POIS:
        poi = Poi.create(**p)
        poi.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        _destroy_data()
        _init_data()

from django.db import models
import uuid
from math import sqrt
# Create your models here.
from rest_framework.exceptions import ValidationError
from xyinc.utils.Validators import positive_validation


class BasicModel(models.Model):
    pid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    removed_at = models.DateTimeField(default=None, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        abstract = True

    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs)

    @classmethod
    def get(cls, **kwargs):
        kwargs['removed_at__isnull'] = True
        return cls.objects.filter(**kwargs)


class Poi(BasicModel):
    name = models.CharField(max_length=20)
    x = models.PositiveSmallIntegerField(validators=[positive_validation, ])
    y = models.PositiveSmallIntegerField(validators=[positive_validation, ])

    def __str__(self):
        return "{name} ({x}, {y})".format(name=self.name, x=self.x, y=self.y)

    @classmethod
    def create(cls, name, x, y, **kwargs):
        kwargs['name'] = name
        kwargs['x'] = int(x)
        kwargs['y'] = int(y)

        poi = super().create(**kwargs)
        return poi

    @classmethod
    def get(cls, name=None, x=None, y=None, **kwargs):

        if name:
            kwargs['name'] = name

        if x and y:
            kwargs['x'], kwargs['y'] = x, y

        if (not x and y) or (x and not y):
            raise ValidationError("Must be x,y coordinates")

        all_objects = super().get(**kwargs)

        if name:
            return all_objects.first()

        return all_objects

    @classmethod
    def search(cls, x, y, radius, **kwargs):
        x, y, radius = int(x), int(y), int(radius)

        return cls.point_distance(px=x, py=y, radius=radius, queryset=cls.get())

    @staticmethod
    def point_distance(px, py, radius,  queryset):
        for p in queryset:
            if sqrt(pow(p.x - px, 2) + pow(p.y - py, 2)) < radius:
                yield p
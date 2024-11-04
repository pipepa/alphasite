from django.db import models
from django.db.models import F
from colorfield.fields import ColorField
from random import randbytes
from django.utils.translation import gettext_lazy as _

class Naming:
    divisions = (
        (1, "1садн"),
        (2, "2садн"),
        (3, "1адн"),
        (4, "2адн"),
        (5, "реабатр"),
    )
    batterys = (
        (1, "1сабатр"),
        (2, "2сабатр"),
        (3, "3сабатп"),
        (4, "1абатр"),
        (5, "2абатр"),
        (6, "3абатр"),
    )

class FirePosition(models.Model):
    name = models.CharField(max_length=20, verbose_name="Назва", unique=True)
    division = models.SmallIntegerField(choices=Naming().divisions, default=1, verbose_name="Підрозділ")
    battery = models.SmallIntegerField(choices=Naming().batterys, default=1, verbose_name="Батерея")
    coordinates = models.CharField(max_length=30, verbose_name="Координати", unique=True)
    left_dgress = models.DecimalField(max_digits=4, decimal_places=0, verbose_name="Кут вліво")
    right_dgress = models.DecimalField(max_digits=4, decimal_places=0, verbose_name="Кут вправо")
    status = models.BooleanField(default=True, verbose_name="Статус")

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Вогнева позиція %s>' % self.name

    class Meta:
        verbose_name = "вогнева позиція"
        verbose_name_plural = "вогневі позиції"

def get_color():
    return randbytes(3).hex()



class Shells(models.Model):
    name = models.CharField(max_length=20, verbose_name="Назва", unique=True)
    color = ColorField(verbose_name="Колір", default=get_color())

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Снаряд %s>' % self.name

    class Meta:
        verbose_name = "Снаряд"
        verbose_name_plural = "Снаряди"


class Powders(models.Model):
    name = models.CharField(max_length=20, verbose_name="Назва", unique=True)
    color = ColorField(default='#FF0000', verbose_name="Колір")

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Заряд %s>' % self.name

    class Meta:
        verbose_name = "Заряд"
        verbose_name_plural = "Заряди"
"""powder_names = [
    "M119(А1/A2)", "M3A1", "М4(А1/A2)", "F1", "BB HB",
    "DM72", "TC-F", "TCME(100)", "TCMSIL", "TCM-C",
    "М231", "М232", "М64A1", "М92", "M203",
    "NR13C1", "L10-A1", "CH8", "KTA5928", "KTA5933"
]
powders_to_create = [Powders(name=name) for name in powder_names]

# Виконання bulk_create
Powders.objects.bulk_create(powders_to_create)"""
#ємо всі снаряди з бази даних


class TablesFire(models.Model):
    shells = Shells.objects.all()
    shell_choices = [(shell.name, shell.name) for shell in shells]
    powders = Powders.objects.all()
    
    powders_choices = [(powder.name, powder.name) for powder in powders]
    number_powder = [(x, x) for x in ["Без номеру", '1', '2', '3', '4', '5', '6', '7']]
    additional_powders_choices = [(powder.name, powder.name) for powder in powders]

    shell = models.CharField(max_length=50, choices=shell_choices, verbose_name="Снаряд", default=1)
    arc_shell = models.BooleanField(verbose_name="АРС", default=False)
    powder = models.CharField(max_length=50, choices=powders_choices, verbose_name="Заряд", default=1)
    number_powder = models.CharField(max_length=50, choices=number_powder, verbose_name="Номер заряду", default="Без номеру")
    additional_powder = models.CharField(max_length=50, choices=additional_powders_choices, verbose_name="Додатковий заряд", blank=True)
    min_distance = models.FloatField(verbose_name="Мінімальна відстань для розрахунків")
    max_distance = models.FloatField(verbose_name="Максимальна відстань для розрахунків")
    def __str__(self):
        number = self.number_powder
        if number == "Без номеру": number = ""
        else:
            number = f" заряд ({number})"
        if self.additional_powder:
            return f"{self.shell} з {self.powder} + {self.additional_powder}"
        else:
            return f"{self.shell} з {self.powder}{number}"
    class Meta:
        verbose_name = "залежність"
        verbose_name_plural = "залежності"

    @classmethod
    def get_filtered_shell_choices(cls, selected_shell):
        return cls.objects.filter(shell=selected_shell)
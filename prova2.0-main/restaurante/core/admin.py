
# core/admin.py
from django.contrib import admin
from .models import Cliente, Mesa, Reserva
from .models import Comida, Pedido

admin.site.register(Cliente)
admin.site.register(Mesa)
admin.site.register(Reserva)
admin.site.register(Comida)
admin.site.register(Pedido)

from django.contrib import admin
from .models import CarspaceModel,TyreModel,Carplan,User
# Register your models here.
admin.site.register(CarspaceModel)
admin.site.register(TyreModel)
admin.site.register(Carplan)

admin.site.register(User)


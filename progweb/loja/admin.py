from django.contrib import admin
from .models import * #imporata nossos models

admin.site.register(Fabricante) 
admin.site.register(Produto)
admin.site.register(Categoria)  
#adiciona a interface do adm
# Register your models here.

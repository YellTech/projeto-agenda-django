from django.contrib import admin
from contact import models 


# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone',)
    ordering = ('-id',)
    search_fields = ('id', 'first_name', 'last_name')
    list_per_page = 15
    list_max_show_all = 150
    list_display_links = ('first_name',)
    # list_filter = 'created_date' --- criar um menu filtro de acordo com o dado da variavel
    # list_editable = ('first_name', 'last_name',) -- Criar campos editaveis de acrodo com os dados da tupla

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    name = ('name',)
    ordering = ('-id',)
    
from django import template
from pages.models import Page

register = template.Library()

@register.simple_tag

#obtener la la lista de paginas
def get_page_list():
    pages = Page.objects.all()
    return pages
from django import template
from shop.models import *

register = template.Library()

@register.filter(name='has_child')
def has_child(id):
    cat = Category.objects.get(id=id)
    child = Category.objects.filter(parent=cat)
    if child:
        return True
    else:
        return False    

@register.filter(name='getchild')
def get_child(id, current_id):
    parent = Category.objects.get(id=id)
    cats = Category.objects.filter(parent=parent)
    html = f'<ul>'
    for cat in cats:
        ch_html = has_child(cat.id)
        child = 'has-child' if ch_html else ''
        active = 'active' if current_id == cat.id else ''
        if child and active:
            html += f'<li class="{child} {active}"><a href="/category/{cat.slug}/">{cat.title}</a>'
        elif child:
            html += f'<li class="{child}"><a href="/category/{cat.slug}/">{cat.title}</a>'
        elif active:
            html += f'<li class="{active}"><a href="/category/{cat.slug}/">{cat.title}</a>'
        else:
            html += f'<li><a href="/category/{cat.slug}/">{cat.title}</a>'
        if ch_html:
            html += get_child(cat.id, current_id)
        html += f'</li>'
    html += f'</ul>'
    return html

@register.filter(name='breadcrumb')
def breadcrumb(id):
    cat = Category.objects.get(id=id)
    parent = cat.parent
    html = ''
    if parent:
        gr_parent = breadcrumb(parent.id)
        if gr_parent:
            html += gr_parent
        html += f'<li><a href="">{parent.title}</a></li><i class="fa-thin fa-angles-right"></i>'
    return html



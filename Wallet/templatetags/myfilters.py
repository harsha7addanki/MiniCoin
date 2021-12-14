from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'aria-describedby': 'basic-addon1','class': arg})

@register.filter(name='addclassi')
def addclass(value, arg):
    return value.as_widget(attrs={'aria-describedby': 'basic-addon1','class': arg, 'id': "yes"})
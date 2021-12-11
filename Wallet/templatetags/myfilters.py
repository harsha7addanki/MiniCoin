from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='labeld')
def labeld(value, arg):
    return value.as_widget(attrs={'aria-describedby': arg})
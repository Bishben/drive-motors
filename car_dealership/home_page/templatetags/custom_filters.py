from django import template

register = template.Library()

# @register.filter(name= 'price')
def price(value):
    return ("AED " + str(value))

register.filter('price',price)

def km(value):
    return (str(value) + " km")

register.filter('km',km)

def createUrl(value):
    return("home/car/" + value)

register.filter('createUrl',createUrl)

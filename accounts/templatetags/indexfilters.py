from django import template
from contatos.models import Contato

register = template.Library()

@register.filter(name='count_contacts')
def count_contacts(user):
    user_contacts = Contato.objects.filter(contact_creator=user)
    count = 0

    for contact in user_contacts:
        count += 1
        
    return count
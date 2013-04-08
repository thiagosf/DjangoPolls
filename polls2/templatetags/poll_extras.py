from django import template
register = template.Library()

@register.filter(name='calculate')
def calculate(votes, total):
    p = (100 * votes) / total
    return p

@register.filter(name='get_class_progress')
def get_class_progress(votes, total):
    p = calculate(votes, total)

    if p >= 35:
        class_name = 'progress-danger'
    elif p >= 20:
        class_name = 'progress-warning'
    elif p >= 15:
        class_name = 'progress-success'
    else:
        class_name = 'progress-info'

    return class_name
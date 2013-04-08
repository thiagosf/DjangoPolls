__author__ = 'thiago'

import datetime
from mongokit import Document

class Computer(Document):

    structure = {
        'make': unicode,
        'model': unicode,
        'purchase_date': datetime.datetime,
        'cpu_ghz': float,
        }

    validators = {
        'cpu_ghz': lambda x: x > 0,
        'make': lambda x: x.strip(),
        }

    default_values = {
        'purchase_date': datetime.datetime.utcnow,
        }

    use_dot_notation = True

    indexes = [
        {'fields': ['make']},
        ]
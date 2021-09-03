import pint
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError


valid_unit_measurments = ['pounds', 'lbs', 'oz', 'gram']

def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        singel_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"{value} is not a valid unit of measure.")
    except:
        raise ValidationError(f"The {value} is invalid.")

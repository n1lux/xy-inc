from rest_framework.exceptions import ValidationError


class PositiveValidator:
    def __init__(self):
        self.num = None

    def __call__(self, num, **kwargs):
        self.num = num
        if self.num < 0:
            raise ValidationError("Must be a positive number")

    def __repr__(self):
        return "Positive Validation"


def positive_validation(value):
    if value < 0:
        raise ValidationError("Must be a positive number")

    return value
from django.core.exceptions import ValidationError


# class PasswordValidator:
#     def __call__(self, value):
#         special_characters = set('!@#$%^&*()-+=`" "|\/?.>,<\';:"~')

#         if len(value) < 8:
#             raise ValidationError('Password must be at least 8 characters long.')

#         if not any(char in special_characters for char in value):
#             raise ValidationError('Password must contain at least one special character.')

#         if not any(char.isdigit() for char in value):
#             raise ValidationError('Password must contain at least one digit.')

#         if not any(char.isupper() for char in value):
#             raise ValidationError('Password must contain at least one uppercase letter.')

#         if not any(char.islower() for char in value):
#             raise ValidationError('Password must contain at least one lowercase letter.')


def passwordvalidator(value):
        special_characters = set('!@#$%^&*()-+=`" "|\/?.>,<\';:"~')

        if not any(char in special_characters for char in value):
            raise ValidationError('Password must contain at least one special character.')

        elif not any(char.isdigit() for char in value):
            raise ValidationError('Password must contain at least one digit.')

        elif not any(char.isupper() for char in value):
            raise ValidationError('Password must contain at least one uppercase letter.')

        elif not any(char.islower() for char in value):
            raise ValidationError('Password must contain at least one lowercase letter.')

def contactvalidator(value):
     if len(value) < 8:
          raise ValidationError('This field must be at least 8 characters.')

from rest_framework.serializers import ValidationError


def validate_link(value):
    if "youtube.com" not in value:
        raise ValidationError("Ссылка должна быть на YouTube")

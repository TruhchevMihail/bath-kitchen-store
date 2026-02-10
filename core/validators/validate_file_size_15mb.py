from django.core.exceptions import ValidationError


def validate_file_size_15mb(file):
    max_size = 15 * 1024 * 1024  # 15MB
    if file.size > max_size:
        raise ValidationError("Image size must be less than 15MB.")

import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.zip', '.rar', '.7zip']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions are: .zip, .rar, .7zip')

def validate_file_size(value):
    limit_mb = 100
    limit_bytes = limit_mb * 1024 * 1024
    if value.size > limit_bytes:
        raise ValidationError(f"File size should not exceed {limit_mb} megabytes.")
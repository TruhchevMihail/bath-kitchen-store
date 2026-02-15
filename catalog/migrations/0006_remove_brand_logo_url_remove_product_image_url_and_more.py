

import core.validators.validate_file_size_15mb
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_category_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='logo_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='brands/', validators=[core.validators.validate_file_size_15mb.validate_file_size_15mb, django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])]),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', validators=[core.validators.validate_file_size_15mb.validate_file_size_15mb, django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/', validators=[core.validators.validate_file_size_15mb.validate_file_size_15mb, django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])]),
        ),
    ]
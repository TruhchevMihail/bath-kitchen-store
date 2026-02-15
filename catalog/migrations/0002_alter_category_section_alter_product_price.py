

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='section',
            field=models.CharField(choices=[('bath', 'Bath'), ('kitchen', 'Kitchen')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MaxValueValidator(10000.0, 'Price must be less than 10000!'), django.core.validators.MinValueValidator(0.01, 'Price must be greater than zero!')]),
        ),
    ]
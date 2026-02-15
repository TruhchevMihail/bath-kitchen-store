

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_subcategory_unique_subcategory_per_section_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unique_id',
            field=models.CharField(default=1, max_length=40, unique=True),
            preserve_default=False,
        ),
    ]
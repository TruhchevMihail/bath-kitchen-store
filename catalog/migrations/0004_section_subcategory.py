

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_brand_product_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=30, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=60)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='catalog.section')),
            ],
            options={
                'ordering': ('section', 'title'),
                'constraints': [models.UniqueConstraint(fields=('section', 'title'), name='unique_subcategory_per_section'), models.UniqueConstraint(fields=('section', 'slug'), name='unique_subcategory_slug_per_section')],
            },
        ),
    ]
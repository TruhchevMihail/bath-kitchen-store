

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjestPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.SlugField(blank=True, max_length=160, unique=True)),
                ('excerpt', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('cover_image_url', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('related_products', models.ManyToManyField(blank=True, related_name='projects', to='catalog.product')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
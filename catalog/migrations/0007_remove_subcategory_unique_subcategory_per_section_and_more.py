

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_brand_logo_url_remove_product_image_url_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='subcategory',
            name='unique_subcategory_per_section',
        ),
        migrations.RemoveConstraint(
            model_name='subcategory',
            name='unique_subcategory_slug_per_section',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('section', 'title'), name='unique_category_title_per_section'),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('section', 'slug'), name='unique_category_slug_per_section'),
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='section',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
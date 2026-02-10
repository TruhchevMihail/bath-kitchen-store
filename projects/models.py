from django.db import models
from django.utils.text import slugify
from catalog.models import Product


class ProjestPost(models.Model):
    title = models.CharField(
        max_length=140,
    )

    slug = models.SlugField(
        max_length=160,
        unique=True,
        blank=True,
    )

    excerpt = models.CharField(
        max_length=255,
    )

    content = models.TextField(
        blank=True,
    )

    cover_image_url = models.URLField(
        blank=True,
    )

    related_products = models.ManyToManyField(
        Product,
        blank=True,
        related_name='projects',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = (
            '-created_at',
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

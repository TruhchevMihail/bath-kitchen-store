from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from core.validators.validate_file_size_15mb import validate_file_size_15mb


class Brand(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True,
    )
    slug = models.SlugField(
        max_length=70,
        unique=True,
        blank=True,
    )
    logo = models.ImageField(
        upload_to="brands/",
        blank=True,
        null=True,
        validators=[
            validate_file_size_15mb,
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"]),
        ],
    )

    def get_absolute_url(self):
        return reverse("brand_detail", kwargs={"brand_slug": self.slug})

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    BATH = 'bath'
    KITCHEN = 'kitchen'

    SECTION_CHOICES = [
        (BATH, 'Bath'),
        (KITCHEN, 'Kitchen'),
    ]

    title = models.CharField(
        max_length=50,
    )
    slug = models.SlugField(
        max_length=50,
        blank=True,
    )
    section = models.CharField(
        max_length=10,
        choices=SECTION_CHOICES,
    )
    description = models.CharField(
        max_length=255,
        blank=True,
    )

    category_image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True,
        validators=[
            validate_file_size_15mb,
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"]),
        ],
    )



    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = (
            "section",
            "title",
        )

        constraints = [
            models.UniqueConstraint(fields=["section", "title"], name="unique_category_title_per_section"),
            models.UniqueConstraint(fields=["section", "slug"], name="unique_category_slug_per_section"),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_section_display()} * {self.title}"


class Product(models.Model):
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='products',
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
    )

    title = models.CharField(
        max_length=120,
    )

    slug = models.SlugField(
        max_length=140,
        unique=True,
        blank=True,
    )

    unique_id = models.CharField(
        max_length=40,
        unique=True,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MaxValueValidator(10000.00, 'Price must be less than 10000!'),
            MinValueValidator(0.01, 'Price must be greater than zero!'),
        ]
    )

    short_description = models.CharField(
        max_length=255,
        blank=True,
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        validators=[
            validate_file_size_15mb,
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"]),
        ],
    )

    is_featured = models.BooleanField(
        default=False,
    )

    is_promo = models.BooleanField(
        default=False,
    )

    sold_count = models.PositiveIntegerField(
        default=0, 
    )

    created_at = models.DateTimeField(
        auto_now_add=True, 
    )

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = (
            '-created_at',
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(str(self))
            super().save(*args, **kwargs)
            self.slug = f"{base}-{self.pk}"
            return super().save(update_fields=["slug"])
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
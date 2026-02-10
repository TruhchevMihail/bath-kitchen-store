from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
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
    logo_url = models.URLField(
        blank=True,
    )

    class Meta:
        ordering = (
            'name',
        )

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
        unique=True,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
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
        upload_to='category_images/',
        blank=True,
        null=True,
        validators=[validate_file_size_15mb]
    )

    class Meta:
        ordering = (
            "section",
            "title",
        )

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

    image_url = models.URLField(
        blank=True, #TODO add validation and MEDIA Upload
    )

    is_featured = models.BooleanField(
        default=False,
    )

    is_promo = models.BooleanField(
        default=False,
    )

    sold_count = models.PositiveIntegerField(
        default=0, #Will help with top products at the home page
    )

    created_at = models.DateTimeField(
        auto_now_add=True, #Will help with the newest products at the home page
    )


    class Meta:
        ordering = (
            '-created_at',
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args , **kwargs)

    def __str__(self):
        return self.title


class Section(models.Model):
    name = models.CharField(max_length=20, unique=True)   # Bath / Kitchen
    slug = models.SlugField(max_length=30, unique=True, blank=True)

    class Meta:
        ordering = ("name",)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="subcategories")
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, blank=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ("section", "title")
        constraints = [
            models.UniqueConstraint(fields=["section", "title"], name="unique_subcategory_per_section"),
            models.UniqueConstraint(fields=["section", "slug"], name="unique_subcategory_slug_per_section"),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.section.name} * {self.title}"












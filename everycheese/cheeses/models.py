from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField
from django.urls import reverse
from django.conf import settings

class Cheese(TimeStampedModel):
    name = models.CharField("Name of the Cheese", max_length=255)
    slug = AutoSlugField("Cheese Address", unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True)

    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified",
        SOFT = "soft", "Soft",
        SEMI_SOFT = "semi-soft", "Semi-Soft",
        SEMI_HARD = "semi-hard", "Semi-Hard",
        HARD = "hard", "Hard"

    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)

    country_of_origin = CountryField("Country of Origin", blank=True)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    def get_absolute_url(self):
        return reverse("cheeses:detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name
    
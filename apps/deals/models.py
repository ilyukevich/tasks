from django.db import models
from pytils.translit import slugify


class Task(models.Model):
    """Task model"""

    title = models.CharField(
        'Heading',
        default='Default value',
        max_length=100,
        help_text='Give a short title to the task'
    )

    text = models.TextField(
        'Text',
        help_text='Describe the essence of the task'
    )

    slug = models.SlugField(
        'Address for the page with the task',
        max_length=100,
        unique=True,
        blank=True,
        help_text=('Enter the address for the task page.'
                   'Use only Latin letters, numbers, hyphens and underscores')
    )

    image = models.ImageField(
        'Image',
        upload_to='tasks/%Y/%m/%d',
        blank=True,
        null=True,
        help_text='Upload image'
    )

    def __str__(self):
        return self.title

    # Extending the built-in save () method: if the slug field is empty -
    # transliterate the content of the title field into Latin, and
    # cut it to one hundred characters
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:100]
        super().save(*args, **kwargs)

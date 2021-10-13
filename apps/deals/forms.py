from django import forms
from django.core.exceptions import ValidationError
from pytils.translit import slugify

from .models import Task


class TaskCreateForm(forms.ModelForm):
    """Form for creating an assignment"""

    class Meta:
        model = Task
        fields = '__all__'

    # Validation of the slug field
    def clean_slug(self):
        """Handles the case if the slug is not unique"""

        cleaned_data = super().clean()
        slug = cleaned_data['slug']
        if not slug:
            title = cleaned_data['slug']
            slug = slugify(title)[:100]
        if Task.objects.filter(slug=slug).exists():
            raise ValidationError(f'The address "{slug}" already exists, '
                                  'come up with a unique value')
        return slug

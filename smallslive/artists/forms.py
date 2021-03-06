from crispy_forms.helper import FormHelper
from django.forms import ModelForm, SelectMultiple
from .models import Artist


class ArtistAddForm(ModelForm):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'salutation', 'instruments', 'biography', 'website', 'photo')
        widgets = {
            'instruments': SelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super(ArtistAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = 'artist_add'
        self.helper.form_method = 'post'
        self.helper.form_tag = False

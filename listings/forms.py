from django.forms import ModelForm
from .models import Listing, CarModel


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car_model'].queryset = CarModel.objects.none()
        if 'car_make' in self.data:
            try:
                car_make_id = int(self.data.get('car_make'))
                self.fields['car_model'].queryset = CarModel.objects.filter(
                    car_make_id=car_make_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.car_make:
            self.fields['car_model'].queryset = (
                self.instance.car_make.carmodel_set.order_by('name'))

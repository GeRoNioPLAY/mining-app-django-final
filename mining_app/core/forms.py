from django import forms
from django.contrib.auth.models import User
from .models import Algorithm, Exchange, Cryptocurrency, Device, CryptocurrencyPrice, Mining, Hashrates

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class AlgorithmForm(forms.ModelForm):
    class Meta:
        model = Algorithm
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CryptocurrencyForm(forms.ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = ['name', 'network_difficulty', 'block_reward', 'algorithm']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'network_difficulty': forms.NumberInput(attrs={'class': 'form-control'}),
            'block_reward': forms.NumberInput(attrs={'class': 'form-control'}),
            'algorithm': forms.Select(attrs={'class': 'form-control'}),
        }

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['company', 'name', 'cost', 'power_consumption']
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'power_consumption': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CryptocurrencyPriceForm(forms.ModelForm):
    class Meta:
        model = CryptocurrencyPrice
        fields = ['cryptocurrency', 'exchange', 'price']
        widgets = {
            'cryptocurrency': forms.Select(attrs={'class': 'form-control'}),
            'exchange': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class HashratesForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['device'].queryset = Device.objects.filter(created_by=user)

    class Meta:
        model = Hashrates
        fields = ['device', 'algorithm', 'hashrate']
        widgets = {
            'device': forms.Select(attrs={'class': 'form-control'}),
            'algorithm': forms.Select(attrs={'class': 'form-control'}),
            'hashrate': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MiningForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['device'].queryset = Device.objects.filter(created_by=user)
        self.fields['cryptocurrency'].queryset = Cryptocurrency.objects.filter(algorithm__isnull=False)
        self.fields['exchange'].queryset = Exchange.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        device = cleaned_data.get('device')
        cryptocurrency = cleaned_data.get('cryptocurrency')
        exchange = cleaned_data.get('exchange')

        if device and cryptocurrency and cryptocurrency.algorithm:
            device_algorithm = Hashrates.objects.filter(
                device=device, algorithm=cryptocurrency.algorithm
            ).first()
            if not device_algorithm:
                raise forms.ValidationError(
                    f"Устройство {device} не поддерживает алгоритм {cryptocurrency.algorithm}. Добавьте хешрейт в таблицу 'Хешрейт'."
                )
            cleaned_data['hashrate'] = device_algorithm.hashrate

        if cryptocurrency and exchange:
            if not CryptocurrencyPrice.objects.filter(
                cryptocurrency=cryptocurrency, exchange=exchange
            ).exists():
                raise forms.ValidationError(
                    f"Биржа {exchange} не имеет цены для криптовалюты {cryptocurrency}."
                )

        return cleaned_data

    class Meta:
        model = Mining
        fields = ['device', 'cryptocurrency', 'exchange']
        widgets = {
            'device': forms.Select(attrs={'class': 'form-control'}),
            'cryptocurrency': forms.Select(attrs={'class': 'form-control'}),
            'exchange': forms.Select(attrs={'class': 'form-control'}),
        }
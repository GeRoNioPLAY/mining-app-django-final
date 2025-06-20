from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from collections import defaultdict
from .models import Algorithm, Exchange, Cryptocurrency, Device, CryptocurrencyPrice, Mining, Hashrates
from .forms import AlgorithmForm, ExchangeForm, CryptocurrencyForm, DeviceForm, CryptocurrencyPriceForm, MiningForm, UserProfileForm, HashratesForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно! Добро пожаловать!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлён.')
            return redirect('profile')
        else:
            messages.error(request, 'Ошибка при обновлении профиля. Проверьте введённые данные.')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'core/profile.html', {'form': form})

def home(request):
    return render(request, 'core/home.html')

def algorithms(request):
    algorithms = Algorithm.objects.all()
    return render(request, 'core/algorithms.html', {'algorithms': algorithms})

@login_required
def algorithm_create(request):
    if not request.user.is_staff:
        messages.error(request, 'Только админы могут создавать алгоритмы.')
        return redirect('algorithms')
    if request.method == 'POST':
        form = AlgorithmForm(request.POST)
        if form.is_valid():
            algorithm = form.save(commit=False)
            algorithm.created_by = request.user
            algorithm.save()
            messages.success(request, 'Алгоритм создан.')
            return redirect('algorithms')
    else:
        form = AlgorithmForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Создать алгоритм'})

@login_required
def algorithm_edit(request, pk):
    algorithm = get_object_or_404(Algorithm, pk=pk)
    if not request.user.is_staff and algorithm.created_by != request.user:
        messages.error(request, 'Вы не можете редактировать этот алгоритм.')
        return redirect('algorithms')
    if request.method == 'POST':
        form = AlgorithmForm(request.POST, instance=algorithm)
        if form.is_valid():
            form.save()
            messages.success(request, 'Алгоритм обновлён.')
            return redirect('algorithms')
    else:
        form = AlgorithmForm(instance=algorithm)
    return render(request, 'core/form.html', {'form': form, 'title': 'Редактировать алгоритм'})

@login_required
def algorithm_delete(request, pk):
    algorithm = get_object_or_404(Algorithm, pk=pk)
    if not request.user.is_staff and algorithm.created_by != request.user:
        messages.error(request, 'Вы не можете удалить этот алгоритм.')
        return redirect('algorithms')
    if request.method == 'POST':
        algorithm.delete()
        messages.success(request, 'Алгоритм удалён.')
        return redirect('algorithms')
    return render(request, 'core/confirm_delete.html', {'object': algorithm, 'title': 'Удалить алгоритм'})

def exchanges(request):
    exchanges = Exchange.objects.all()
    return render(request, 'core/exchanges.html', {'exchanges': exchanges})

@login_required
def exchange_create(request):
    if not request.user.is_staff:
        messages.error(request, 'Только админы могут создавать биржи.')
        return redirect('exchanges')
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            exchange = form.save(commit=False)
            exchange.created_by = request.user
            exchange.save()
            messages.success(request, 'Биржа создана.')
            return redirect('exchanges')
    else:
        form = ExchangeForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Создать биржу'})

@login_required
def exchange_edit(request, pk):
    exchange = get_object_or_404(Exchange, pk=pk)
    if not request.user.is_staff and exchange.created_by != request.user:
        messages.error(request, 'Вы не можете редактировать эту биржу.')
        return redirect('exchanges')
    if request.method == 'POST':
        form = ExchangeForm(request.POST, instance=exchange)
        if form.is_valid():
            form.save()
            messages.success(request, 'Биржа обновлена.')
            return redirect('exchanges')
    else:
        form = ExchangeForm(instance=exchange)
    return render(request, 'core/form.html', {'form': form, 'title': 'Редактировать биржу'})

@login_required
def exchange_delete(request, pk):
    exchange = get_object_or_404(Exchange, pk=pk)
    if not request.user.is_staff and exchange.created_by != request.user:
        messages.error(request, 'Вы не можете удалить эту биржу.')
        return redirect('exchanges')
    if request.method == 'POST':
        exchange.delete()
        messages.success(request, 'Биржа удалена.')
        return redirect('exchanges')
    return render(request, 'core/confirm_delete.html', {'object': exchange, 'title': 'Удалить биржу'})

def cryptocurrencies(request):
    cryptocurrencies = Cryptocurrency.objects.all()
    return render(request, 'core/cryptocurrencies.html', {'cryptocurrencies': cryptocurrencies})

@login_required
def cryptocurrency_create(request):
    if not request.user.is_staff:
        messages.error(request, 'Только админы могут создавать криптовалюты.')
        return redirect('cryptocurrencies')
    if request.method == 'POST':
        form = CryptocurrencyForm(request.POST)
        if form.is_valid():
            crypto = form.save(commit=False)
            crypto.created_by = request.user
            crypto.save()
            messages.success(request, 'Криптовалюта создана.')
            return redirect('cryptocurrencies')
    else:
        form = CryptocurrencyForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Создать криптовалюту'})

@login_required
def cryptocurrency_edit(request, pk):
    crypto = get_object_or_404(Cryptocurrency, pk=pk)
    if not request.user.is_staff and crypto.created_by != request.user:
        messages.error(request, 'Вы не можете редактировать эту криптовалюту.')
        return redirect('cryptocurrencies')
    if request.method == 'POST':
        form = CryptocurrencyForm(request.POST, instance=crypto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Криптовалюта обновлена.')
            return redirect('cryptocurrencies')
    else:
        form = CryptocurrencyForm(instance=crypto)
    return render(request, 'core/form.html', {'form': form, 'title': 'Редактировать криптовалюту'})

@login_required
def cryptocurrency_delete(request, pk):
    crypto = get_object_or_404(Cryptocurrency, pk=pk)
    if not request.user.is_staff and crypto.created_by != request.user:
        messages.error(request, 'Вы не можете удалить эту криптовалюту.')
        return redirect('cryptocurrencies')
    if request.method == 'POST':
        crypto.delete()
        messages.success(request, 'Криптовалюта удалена.')
        return redirect('cryptocurrencies')
    return render(request, 'core/confirm_delete.html', {'object': crypto, 'title': 'Удалить криптовалюту'})

def devices(request):
    devices = Device.objects.all()
    return render(request, 'core/devices.html', {'devices': devices})

@login_required
def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.created_by = request.user
            device.save()
            messages.success(request, 'Устройство создано.')
            return redirect('devices')
    else:
        form = DeviceForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Создать устройство'})

@login_required
def device_edit(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if not request.user.is_staff and device.created_by != request.user:
        messages.error(request, 'Вы не можете редактировать это устройство.')
        return redirect('devices')
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            messages.success(request, 'Устройство обновлено.')
            return redirect('devices')
    else:
        form = DeviceForm(instance=device)
    return render(request, 'core/form.html', {'form': form, 'title': 'Редактировать устройство'})

@login_required
def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if not request.user.is_staff and device.created_by != request.user:
        messages.error(request, 'Вы не можете удалить это устройство.')
        return redirect('devices')
    if request.method == 'POST':
        device.delete()
        messages.success(request, 'Устройство удалено.')
        return redirect('devices')
    return render(request, 'core/confirm_delete.html', {'object': device, 'title': 'Удалить устройство'})

def crypto_list(request):
    cryptocurrencies = CryptocurrencyPrice.objects.all()
    return render(request, 'core/crypto_list.html', {'cryptocurrencies': cryptocurrencies})

@login_required
def crypto_price_create(request):
    if request.method == 'POST':
        form = CryptocurrencyPriceForm(request.POST)
        if form.is_valid():
            price = form.save(commit=False)
            price.created_by = request.user
            price.save()
            messages.success(request, 'Цена криптовалюты добавлена.')
            return redirect('crypto_list')
    else:
        form = CryptocurrencyPriceForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Добавить цену криптовалюты'})

@login_required
def crypto_price_edit(request, pk):
    price = get_object_or_404(CryptocurrencyPrice, pk=pk)
    if not request.user.is_staff and price.created_by != request.user:
        messages.error(request, 'Вы не можете редактировать эту цену.')
        return redirect('crypto_list')
    if request.method == 'POST':
        form = CryptocurrencyPriceForm(request.POST, instance=price)
        if form.is_valid():
            form.save()
            messages.success(request, 'Цена обновлена.')
            return redirect('crypto_list')
    else:
        form = CryptocurrencyPriceForm(instance=price)
    return render(request, 'core/form.html', {'form': form, 'title': 'Редактировать цену криптовалюты'})

@login_required
def crypto_price_delete(request, pk):
    price = get_object_or_404(CryptocurrencyPrice, pk=pk)
    if not request.user.is_staff and price.created_by != request.user:
        messages.error(request, 'Вы не можете удалить эту цену.')
        return redirect('crypto_list')
    if request.method == 'POST':
        price.delete()
        messages.success(request, 'Цена удалена.')
        return redirect('crypto_list')
    return render(request, 'core/confirm_delete.html', {'object': price, 'title': 'Удалить цену криптовалюты'})

def hashrates(request):
    hashrates = Hashrates.objects.all()
    return render(request, 'core/hashrates.html', {'hashrates': hashrates})

@login_required
def hashrates_create(request):
    if request.method == 'POST':
        form = HashratesForm(request.user, request.POST)
        if form.is_valid():
            device_algorithm = form.save(commit=False)
            device_algorithm.created_by = request.user
            device_algorithm.save()
            messages.success(request, 'Хэшрейт создан.')
            return redirect('hashrates')
    else:
        form = HashratesForm(user=request.user)
    return render(request, 'core/form.html', {'form': form, 'title': 'Создать хэшрейт'})

@login_required
def hashrates_edit(request, pk):
    device_algorithm = get_object_or_404(Hashrates, pk=pk)
    if not request.user.is_staff and device_algorithm.created_by != request.user:
        messages.error(request, 'Вы не можете редактировать этот хэшрейт.')
        return redirect('hashrates')
    if request.method == 'POST':
        form = HashratesForm(request.user, request.POST, instance=device_algorithm)
        if form.is_valid():
            form.save()
            messages.success(request, 'Хэшрейт обновлён.')
            return redirect('hashrates')
    else:
        form = HashratesForm(request.user, instance=device_algorithm)
    return render(request, 'core/form.html', {'form': form, 'title': 'Редактировать хэшрейт'})

@login_required
def hashrates_delete(request, pk):
    device_algorithm = get_object_or_404(Hashrates, pk=pk)
    if not request.user.is_staff and device_algorithm.created_by != request.user:
        messages.error(request, 'Вы не можете удалить этот хэшрейт.')
        return redirect('hashrates')
    if request.method == 'POST':
        device_algorithm.delete()
        messages.success(request, 'Хэшрейт удалён.')
        return redirect('hashrates')
    return render(request, 'core/confirm_delete.html', {'object': device_algorithm, 'title': 'Удалить хэшрейт'})

def mining(request):
    if not request.user.is_authenticated:
        return render(request, 'core/mining.html', {'mining_sessions': [], 'user_sessions': [], 'total_mined_per_hour': 0, 'total_power_consumption': 0, 'total_rubles_per_hour': 0})

    mining_sessions = Mining.objects.filter(created_by=request.user)
    user_sessions = mining_sessions

    total_mined_per_hour = 0
    total_power_consumption = 0
    crypto_mined_per_hour = defaultdict(float)
    crypto_rubles_per_hour = defaultdict(float)
    total_rubles_per_hour = 0

    for session in mining_sessions:
        if session.cryptocurrency and session.exchange:
            price_obj = CryptocurrencyPrice.objects.filter(
                cryptocurrency=session.cryptocurrency,
                exchange=session.exchange
            ).first()
            setattr(session, 'price', price_obj.price if price_obj else None)
        if session.device and session.cryptocurrency and session.cryptocurrency.algorithm:
            hasrate_obj = Hashrates.objects.filter(
                device=session.device,
                algorithm=session.cryptocurrency.algorithm
            ).first()
            setattr(session, 'hashrate_value', hasrate_obj.hashrate if hasrate_obj else None)

            if getattr(session, 'hashrate_value') and session.cryptocurrency.block_reward and session.cryptocurrency.network_difficulty:
                mined_per_second = (getattr(session, 'hashrate_value') * session.cryptocurrency.block_reward) / (session.cryptocurrency.network_difficulty * (2 ** 32))
                mined_per_hour = mined_per_second * 3600
                total_mined_per_hour += mined_per_hour
                crypto_name = session.cryptocurrency.name
                crypto_mined_per_hour[crypto_name] += mined_per_hour
                if session.price:
                    rubles_per_hour = mined_per_hour * session.price
                    crypto_rubles_per_hour[crypto_name] += rubles_per_hour
                    total_rubles_per_hour += rubles_per_hour
                else:
                    setattr(session, 'rubles_per_hour', 0)
            else:
                setattr(session, 'hashrate_value', None)
                setattr(session, 'rubles_per_hour', 0)
        else:
            setattr(session, 'hashrate_value', None)
            setattr(session, 'rubles_per_hour', 0)
        total_power_consumption += session.device.power_consumption or 0

    crypto_data = []
    for crypto, mined in crypto_mined_per_hour.items():
        rubles = crypto_rubles_per_hour.get(crypto, 0)
        crypto_data.append((crypto, mined, rubles))

    context = {
        'mining_sessions': mining_sessions,
        'user_sessions': user_sessions,
        'total_mined_per_hour': total_mined_per_hour,
        'total_power_consumption': total_power_consumption,
        'total_rubles_per_hour': total_rubles_per_hour,
        'crypto_data': crypto_data,
    }
    return render(request, 'core/mining.html', context)

@login_required
def mining_create(request):
    if request.method == 'POST':
        form = MiningForm(request.user, request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.created_by = request.user
            session.save()
            messages.success(request, 'Сессия майнинга создана.')
            return redirect('mining')
        else:
            messages.error(request, 'Ошибка создания сессии. Проверь данные.')
    else:
        form = MiningForm(user=request.user)
    return render(request, 'core/form.html', {'form': form, 'title': 'Создать сессию майнинга'})

@login_required
def mining_edit(request, pk):
    session = get_object_or_404(Mining, pk=pk)
    if not request.user.is_staff and session.created_by != request.user:
        messages.error(request, 'Вы не можете редактировать эту сессию.')
        return redirect('mining')
    if request.method == 'POST':
        form = MiningForm(request.user, request.POST, instance=session)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сессия обновлена.')
            return redirect('mining')
        else:
            messages.error(request, 'Ошибка обновления сессии. Проверь данные.')
    else:
        form = MiningForm(request.user, instance=session)
    return render(request, 'core/form.html', {'form': form, 'title': 'Редактировать сессию майнинга'})

@login_required
def mining_delete(request, pk):
    session = get_object_or_404(Mining, pk=pk)
    if not request.user.is_staff and session.created_by != request.user:
        messages.error(request, 'Вы не можете удалить эту сессию.')
        return redirect('mining')
    if request.method == 'POST':
        session.delete()
        messages.success(request, 'Сессия удалена.')
        return redirect('mining')
    return render(request, 'core/confirm_delete.html', {'object': session, 'title': 'Удалить сессию майнинга'})
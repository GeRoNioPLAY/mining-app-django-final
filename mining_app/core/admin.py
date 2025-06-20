from django.contrib import admin
from .models import Algorithm, Exchange, Cryptocurrency, Device, CryptocurrencyPrice, Mining, Hashrates

@admin.register(Algorithm)
class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    list_filter = ('created_by', 'created_at')
    search_fields = ('name',)

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    list_filter = ('created_by', 'created_at')
    search_fields = ('name',)

@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'network_difficulty', 'block_reward', 'algorithm', 'created_by', 'created_at')
    list_filter = ('algorithm', 'created_by', 'created_at')
    search_fields = ('name',)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'cost', 'power_consumption', 'created_by', 'created_at')
    list_filter = ('company', 'created_by', 'created_at')
    search_fields = ('name', 'company')

@admin.register(CryptocurrencyPrice)
class CryptocurrencyPriceAdmin(admin.ModelAdmin):
    list_display = ('cryptocurrency', 'exchange', 'price', 'created_by', 'created_at')
    list_filter = ('cryptocurrency', 'exchange', 'created_by', 'created_at')
    search_fields = ('cryptocurrency__name', 'exchange__name')

@admin.register(Hashrates)
class HashratesAdmin(admin.ModelAdmin):
    list_display = ('device', 'algorithm', 'hashrate', 'created_by', 'created_at')
    list_filter = ('device', 'created_by', 'created_at')
    search_fields = ('device__name', 'algorithm__name', 'hashrate__name')

@admin.register(Mining)
class MiningAdmin(admin.ModelAdmin):
    list_display = ['device', 'cryptocurrency', 'exchange', 'get_price', 'get_hashrate', 'get_block_reward', 'get_network_difficulty', 'created_by', 'created_at']
    list_filter = ['device', 'cryptocurrency', 'exchange', 'created_by', 'created_at']
    search_fields = ['device__name', 'cryptocurrency__name', 'exchange__name']

    def get_price(self, obj):
        price = CryptocurrencyPrice.objects.filter(cryptocurrency=obj.cryptocurrency, exchange=obj.exchange).first()
        return price.price if price else 'Нет цены'
    get_price.short_description = 'Цена'

    def get_hashrate(self, obj):
        device_algorithm = Hashrates.objects.filter(device=obj.device, algorithm=obj.cryptocurrency.algorithm).first()
        return device_algorithm.hashrate if device_algorithm else 'Нет хешрейта'
    get_hashrate.short_description = 'Хешрейт'

    def get_block_reward(self, obj):
        return obj.cryptocurrency.block_reward if obj.cryptocurrency else 'Нет награды'
    get_block_reward.short_description = 'Награда за блок'

    def get_network_difficulty(self, obj):
        return obj.cryptocurrency.network_difficulty if obj.cryptocurrency else 'Нет сложности'
    get_network_difficulty.short_description = 'Сложность сети'
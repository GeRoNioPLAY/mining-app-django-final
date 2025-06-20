from django.db import models
from django.contrib.auth.models import User

class Algorithm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='algorithms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Алгоритм"
        verbose_name_plural = "Алгоритмы"
        
class Exchange(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='exchanges')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Биржа"
        verbose_name_plural = "Биржи"
        
class Cryptocurrency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    network_difficulty = models.FloatField()
    block_reward = models.FloatField()
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE, null=True, related_name='cryptocurrencies')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cryptocurrencies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Криптовалюта"
        verbose_name_plural = "Криптовалюты"
        
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    cost = models.FloatField()
    power_consumption = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='devices')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} {self.name}"

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"
        
class CryptocurrencyPrice(models.Model):
    id = models.AutoField(primary_key=True)
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE, null=True, related_name='prices')
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE, null=True, related_name='prices')
    price = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cryptocurrency_prices')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cryptocurrency.name} on {self.exchange.name}: {self.price}"

    class Meta:
        verbose_name = "Цена криптовалюты"
        verbose_name_plural = "Цены криптовалют"


class Hashrates(models.Model):
    id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, related_name='device_algorithms')
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE, null=True, related_name='device_algorithms')
    hashrate = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='device_algorithms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device} - {self.algorithm.name} ({self.hashrate} H/s)"

    class Meta:
        verbose_name = "Хешрейты"
        verbose_name_plural = "Хешрейты"

class Mining(models.Model):
    id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, related_name='mining_sessions')
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE, null=True, related_name='mining_sessions')
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE, null=True, related_name='mining_sessions')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='mining_sessions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device} - {self.cryptocurrency.name}"

    class Meta:
        verbose_name = "Сессия майнинга"
        verbose_name_plural = "Сессии майнинга"
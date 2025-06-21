from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from core.models import Exchange, Mining

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'exchanges', 'mining', 'profile']

    def location(self, item):
        return reverse(item)

class ExchangeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Exchange.objects.all()

    def location(self, obj):
        return reverse('exchange_detail', args=[obj.pk])

class MiningSessionSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.7

    def items(self):
        return Mining.objects.all()

    def location(self, obj):    
        return reverse('mining_session_detail', args=[obj.pk])
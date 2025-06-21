from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from core.sitemaps import StaticViewSitemap, ExchangeSitemap, MiningSessionSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'exchanges': ExchangeSitemap,
    'mining_sessions': MiningSessionSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('algorithms/', views.algorithms, name='algorithms'),
    path('algorithms/create/', views.algorithm_create, name='algorithm_create'),
    path('algorithms/edit/<int:pk>/', views.algorithm_edit, name='algorithm_edit'),
    path('algorithms/delete/<int:pk>/', views.algorithm_delete, name='algorithm_delete'),
    path('exchanges/', views.exchanges, name='exchanges'),
    path('exchanges/create/', views.exchange_create, name='exchange_create'),
    path('exchanges/edit/<int:pk>/', views.exchange_edit, name='exchange_edit'),
    path('exchanges/delete/<int:pk>/', views.exchange_delete, name='exchange_delete'),
    path('cryptocurrencies/', views.cryptocurrencies, name='cryptocurrencies'),
    path('cryptocurrencies/create/', views.cryptocurrency_create, name='cryptocurrency_create'),
    path('cryptocurrencies/edit/<int:pk>/', views.cryptocurrency_edit, name='cryptocurrency_edit'),
    path('cryptocurrencies/delete/<int:pk>/', views.cryptocurrency_delete, name='cryptocurrency_delete'),
    path('devices/', views.devices, name='devices'),
    path('devices/create/', views.device_create, name='device_create'),
    path('devices/edit/<int:pk>/', views.device_edit, name='device_edit'),
    path('devices/delete/<int:pk>/', views.device_delete, name='device_delete'),
    path('crypto-list/', views.crypto_list, name='crypto_list'),
    path('crypto-list/create/', views.crypto_price_create, name='crypto_price_create'),
    path('crypto-list/edit/<int:pk>/', views.crypto_price_edit, name='crypto_price_edit'),
    path('crypto-list/delete/<int:pk>/', views.crypto_price_delete, name='crypto_price_delete'),
    path('mining/', views.mining, name='mining'),
    path('mining/create/', views.mining_create, name='mining_create'),
    path('mining/edit/<int:pk>/', views.mining_edit, name='mining_edit'),
    path('mining/delete/<int:pk>/', views.mining_delete, name='mining_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('hashrates/', views.hashrates, name='hashrates'),
    path('hashrates/create/', views.hashrates_create, name='hashrates_create'),
    path('hashrates/edit/<int:pk>/', views.hashrates_edit, name='hashrates_edit'),
    path('hashrates/delete/<int:pk>/', views.hashrates_delete, name='hashrates_delete'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('exchange/<int:pk>/', views.exchanges, name='exchange_detail'),
    path('mining_session/<int:pk>/', views.mining, name='mining_session_detail'),
]

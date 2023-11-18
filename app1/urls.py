from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
 path('home/', views.home_view, name='home_view'),
 path('addpdt/', views.add_product, name='add_product'),
 path('addexp/', views.add_expense, name='add_expense'),
 path('dash_view/', views.dash_view, name='dash_view'),
 path('store/', views.store_view, name='store_view'),
 path('about/', views.about_view, name='about_view'),

]

# Include static and media URL patterns for debug mode
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


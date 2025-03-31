"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import main_page
from password_generator.views import (
    password_generator_page_view,
    PasswordGeneratorAPIView,
)
from timer.views import (
    timer_view,
    StopwatchAPIView,
    TimerAPIView,
)
from qr_coder.views import (
    qr_code_view,
    EncoderAPIView,
    ImageUploadView,
)
from api_weather.views import (
    weather_view,
    WeatherAPIView,
)

from ocr.views import (
    ocr_view,
    ocrAPIView,
)

from pdfcut.views import (
    pdfcutAPIView,
    pdf_view,
)
urlpatterns = [
    path('', main_page, name='main-page'),
    path('admin/', admin.site.urls),
    path('timer/', timer_view, name='timer'),
    path('generate-password/', password_generator_page_view, name='generate-password'),  # noqa
    path('qr-coder/', qr_code_view, name='qr-coder'),
    path('weather/', weather_view, name='weather'),
    path('ocr/', ocr_view, name='ocr'),
    path('pdfcut/', pdf_view, name='pdfcut'),
    path('api/generate-password/', PasswordGeneratorAPIView.as_view(), name='generate-password-api'),  # noqa
    path('api/timer/', TimerAPIView.as_view(), name='timer-api-view'),
    path('api/stopwatch/', StopwatchAPIView.as_view(), name='stopwatch'),
    path('api/weather/', WeatherAPIView.as_view(), name='api-weather'),
    path('api/encoder/', EncoderAPIView.as_view(), name='api-encoder'),
    path('api/upload/', ImageUploadView.as_view(), name='upload'),
    path('api/ocr/', ocrAPIView.as_view(), name='api-ocr'),
    path('api/pdf/', pdfcutAPIView.as_view(), name='api-pdf'),
]

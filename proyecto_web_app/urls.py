from django.urls import path
from proyecto_web_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/",views.home, name="Home"),
    path("bienvenida/", views.bienvenida, name="Bienvenida"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
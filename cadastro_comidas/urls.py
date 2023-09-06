from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Avisando ao projeto que tem um arquivo urls dentro de 'core'
    path('', include('core.urls'))
]

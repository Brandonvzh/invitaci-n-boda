from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'wedding'

urlpatterns = [
    path('guests-data/', view = views.bride_form_view, name = "bride-form-view"),
    path('guests-table/', view = views.guests_table, name = "guests_table"),
    path('guests-data/save_data/<str:pk>', view = views.update_data, name = "update_data"),
    path('x/', view = views.copy_data, name = "x"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

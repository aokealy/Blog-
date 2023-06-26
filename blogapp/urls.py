from django.urls  import path
from .views import CorePageView

urlpatterns = [
    path('', CorePageView.as_view(), name='home'),
]
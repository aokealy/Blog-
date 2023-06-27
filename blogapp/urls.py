from django.urls  import path
from .views import CorePageView, BlogPageView, ContactPageView, AboutPageView

urlpatterns = [
    # Core Page
    path('', CorePageView.as_view(), name='main'),
    
    # blog-section page
    path('blog/', BlogPageView.as_view(), name='blog'),
    
    # Contact Page
    path('contacts/', ContactPageView.as_view(), name='contacts'),

    # About Page
    path('about/', AboutPageView.as_view(), name='about'),
]
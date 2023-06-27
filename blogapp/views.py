from django.views.generic import TemplateView

# Core template page
class CorePageView(TemplateView):
    template_name = 'blogapp/core.html'

# Blog page
class BlogPageView(TemplateView):
    template_name = 'blogapp/blog-section.html'

# blog section
# class BlogSectionPageView(TemplateView):
#     template_name = 'blogapp/blog-section.html'    



# Contact page
class ContactPageView(TemplateView):
    template_name = 'blogapp/contact.html'

# About page
class AboutPageView(TemplateView):
    template_name = 'blogapp/about.html'
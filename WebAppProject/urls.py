from django.conf.urls import url
from WebAppProject import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^account/', views.account, name='account'),
    url(r'^nearest-gym/', views.nearestgym, name='nearest gym'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^faq/', views.faq, name='faq'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<post_name_slug>[\w\-]+)/$',
        views.show_post, name='show_post'),
]

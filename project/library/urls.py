from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('library',
    url(r'^all$',
        view='views.listing',
        kwargs={'template':'book_listing.html'},
        name='listing'
    ),
    url(r'^library/(?P<id>[-\w]+)/$',
      view='views.book',
      kwargs={'template':'book.html'},
      name='book'
    )
)

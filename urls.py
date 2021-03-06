from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from apps.blog.views import AboutView
from apps.blog.views import ArchiveView
from apps.blog.views import BlogListByCategoryView
from apps.blog.views import BlogListView
from apps.blog.views import LatestPosts
from apps.blog.views import TagListView
from apps.blog.views import CategoryListView
from apps.blog.views import BlogListByTagView
from django_blog.sitemaps import BlogSitemap, IndexSitemap

admin.autodiscover()

sitemaps = {
    'index': IndexSitemap,
    'blog': BlogSitemap,

}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BlogListView.as_view(), name="home"),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^404', TemplateView.as_view(template_name="404.html")),

    url(r"^tag/(?P<tag_name>[\w,-]+)$", BlogListByTagView.as_view(), name="tag"),
    url(r"^category/(?P<pk>\d+)/(?P<cat_name>\w+)$", BlogListByCategoryView.as_view(), name="category"),
    url(r"^tags$", TagListView.as_view(), name="tag_list"),
    url(r"^categories$", CategoryListView.as_view(), name="category_list"),
    url(r"^archives", ArchiveView.as_view(), name="archives"),

    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url(r'^humans.txt$', TemplateView.as_view(template_name="humans.txt", content_type="text/plain")),
    url(r'^rss/', LatestPosts(), name='feeds'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

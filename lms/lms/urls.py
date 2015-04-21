from django.conf.urls import include, url
from django.contrib import admin
from courses.views import CreateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'lms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/create', CreateView.as_view(), name="create_course"),
]

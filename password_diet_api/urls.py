from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from api import views as api_views


router = routers.DefaultRouter()
router.register(r'sitepasswords', api_views.UserViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'password_diet_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token')
]

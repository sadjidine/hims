from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views
from django.urls import path, reverse

# from pprint import pprint

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('specialities', views.SpecialityViewSet)
router.register('codifications', views.CodificationViewSet)
# pprint(router.urls)

# URLConf
urlpatterns = router.urls

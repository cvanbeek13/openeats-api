#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from v1.recipe_groups import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cuisine-count', views.CuisineCountViewSet, base_name='cuisine-count')
router.register(r'cuisine', views.CuisineViewSet, base_name='cuisine')
router.register(r'course-count', views.CourseCountViewSet, base_name='course-count')
router.register(r'course', views.CourseViewSet, base_name='course')
router.register(r'tag-count', views.TagCountViewSet, base_name='tag-count')
router.register(r'tag', views.TagViewSet, base_name='tag') # Not sure if basename needed

urlpatterns = [
    url('', include(router.urls)),
]

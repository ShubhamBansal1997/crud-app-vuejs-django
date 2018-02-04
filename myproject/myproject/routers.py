# -*- coding: utf-8 -*-
# @Author: shubhambansal
# @Date:   2018-02-04 23:08:11
# @Last Modified by:   shubhambansal
# @Last Modified time: 2018-02-04 23:25:39
from rest_framework import routers
from article.viewsets import ArticleViewSet

router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)

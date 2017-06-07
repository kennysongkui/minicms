#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/7 11:03
# @Author  : Kenny Song
# @Site    : 
# @File    : nav_processor.py.py
# @Software: PyCharm

from .models import Column

nav_display_columns = Column.objects.filter(nav_display=True)

def nav_column(request):
    return {'nav_display_columns': nav_display_columns}
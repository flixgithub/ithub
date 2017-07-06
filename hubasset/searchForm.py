# -*- coding:utf8 -*-
from django import forms


class searchForm(forms.Form):
    assetId = forms.CharField()
    bamsId = forms.CharField()
    hostname = forms.CharField()
    ip = forms.CharField()
    ilomIp = forms.CharField()


# coding:utf-8
from __future__ import unicode_literals

from django import forms
from .models import AnalizePlan
from .models import AnalizeRes


class AnalizePlanForm(forms.ModelForm):
    class Meta:
        model = AnalizePlan
        fields = (
            'code', 'status'
        )


class AnalizeResForm(forms.ModelForm):
    class Meta:
        model = AnalizeRes
        fields = (
            'code', 'times', 'success', 'failed'
        )

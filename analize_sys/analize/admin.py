# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import AnalizePlan
from .models import AnalizeRes


class AnalizePlanAdmin(admin.ModelAdmin):
    list_display = ('code', 'start_time', 'end_time', 'status')
    fields = ('code', )
    search_fields = ('code', 'status')
    save_as = False
    save_as_continue = False

    def save_model(self, request, obj, form, change):
        if change:  # 更改的时候
            obj_original = self.model.objects.get(pk=obj.pk)
        else:  # 新增的时候
            obj_original = None

        print(request.user)
        print(obj.code)
        #obj.user = request.user
        obj.save()


class AnalizeAdmin(admin.ModelAdmin):
    list_display = ('code', 'start_time', 'end_time', 'times', 'success', 'failed', 'result')
    fields = ('code', )
    search_fields = ('code', 'result')
    save_as = False
    save_as_continue = False

    def has_add_permission(self, request):
        return False

admin.site.register(AnalizePlan, AnalizePlanAdmin)
admin.site.register(AnalizeRes, AnalizeAdmin)

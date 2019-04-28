# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError


class AnalizePlan(models.Model):
    STATUS_ITEMS = [
        (0, '待分析'),
        (1, '分析中'),
        (2, '分析完成'),
    ]
    code = models.CharField(max_length=128, verbose_name="代码")
    start_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="任务开始时间")
    end_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="任务结束时间")
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="分析状态")

    def __unicode__(self):
        return '<AnalizePlan: {}>'.format(self.code)

    class Meta:
        verbose_name = verbose_name_plural = "趋势分析任务"

    def clean(self):
        if 'csv' not in self.code and 6 != len(self.code):
            raise ValidationError("必须是6位数字或CSV数据")


class AnalizeRes(models.Model):
    RESULT_ITEMS = [
        (0, '向上'),
        (1, '向下'),
        (2, '无法预测'),
    ]

    code = models.CharField(max_length=128, verbose_name="代码")
    start_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="预测开始时间")
    end_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="预测结束时间")
    times = models.IntegerField(default=0,  verbose_name="预测次数")
    success = models.IntegerField(default=0,  verbose_name="预测正确次数")
    failed = models.IntegerField(default=0,  verbose_name="预测错误次数")
    result = models.IntegerField(choices=RESULT_ITEMS, default=0, verbose_name="预测结论")

    def __unicode__(self):
        return '<AnalizeRes: {}>'.format(self.code)

    class Meta:
        verbose_name = verbose_name_plural = "趋势分析结果"

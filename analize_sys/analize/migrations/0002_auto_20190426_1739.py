# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-26 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analize', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analize',
            options={'verbose_name': '趋势分析系统', 'verbose_name_plural': '趋势分析系统'},
        ),
        migrations.AddField(
            model_name='analize',
            name='result',
            field=models.IntegerField(choices=[(0, '向上'), (1, '向下'), (2, '无法预测')], default=0, verbose_name='预测结论'),
        ),
        migrations.AlterField(
            model_name='analize',
            name='code',
            field=models.CharField(max_length=128, verbose_name='代码'),
        ),
        migrations.AlterField(
            model_name='analize',
            name='status',
            field=models.IntegerField(choices=[(0, '分析中'), (1, '分析完成')], default=0, verbose_name='分析状态'),
        ),
    ]

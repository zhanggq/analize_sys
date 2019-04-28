# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from .models import AnalizePlan
from .models import AnalizeRes
from .forms import AnalizePlanForm
from .forms import AnalizeResForm


class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        contexts = AnalizeRes.objects.all()
        context = {
            'students': contexts,
        }
        return context

    def get(self, request):
        context = self.get_context()
        #form = StudentForm()
        form = AnalizeResForm()
        context.update({
            'form': form
        })
        raise Exception('hhh')
        response = render(request, self.template_name, context=context)
        return response

    def post(self, request):
        form = AnalizeResForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            #student = Student()
            #student.name = cleaned_data['name']
            #student.sex = cleaned_data['sex']
            #student.email = cleaned_data['email']
            #student.profession = cleaned_data['profession']
            #student.qq = cleaned_data['qq']
            #student.phone = cleaned_data['phone']
            #student.save()
            analize = AnalizeRes()
            analize.code = cleaned_data['code']
            analize.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

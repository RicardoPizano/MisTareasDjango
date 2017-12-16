# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SemesterYear(models.Model):
    user = models.ForeignKey()
    number = models.PositiveIntegerField()
    is_finish = models.BooleanField()
    is_active = models.BooleanField()
    register_date = models.DateField(auto_now_add=True)
    delete_date = models.DateField(null=True, blank=True)


class SchoolSubject(models.Model):
    semester_year = models.ForeignKey(SemesterYear)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    teacher = models.CharField(max_length=100)
    color = models.CharField(max_length=7)
    is_active = models.BooleanField()
    register_date = models.DateField(auto_now_add=True)
    delete_date = models.DateField(null=True, blank=True)


class SchoolSchedule(models.Model):
    school_subject = models.ForeignKey(SchoolSubject)
    day = models.ImageField()
    classroom = models.CharField(max_length=20)
    entry_time = models.TimeField()
    departure_time = models.TimeField()
    classroom_abbreviation = models.CharField(max_length=5)
    is_active = models.BooleanField()
    register_date = models.DateField(auto_now_add=True)
    delete_date = models.DateField(null=True, blank=True)

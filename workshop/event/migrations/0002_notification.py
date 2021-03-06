# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_text', models.CharField(help_text='Notification Text', max_length=10000)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
            options={
                'ordering': ['-event'],
                'verbose_name_plural': 'Notifications',
                'verbose_name': 'Notification',
            },
        ),
    ]

# Generated by Django 3.0.4 on 2020-09-27 00:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_credit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='images/')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Redeemed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redeemed_on', models.DateField(default=datetime.datetime(2020, 9, 27, 0, 6, 17, 896692, tzinfo=utc))),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Gifts')),
                ('redeemed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

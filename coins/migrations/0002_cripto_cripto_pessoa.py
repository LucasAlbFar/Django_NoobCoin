# Generated by Django 3.2.3 on 2021-07-18 17:13

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cripto',
            name='cripto_pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

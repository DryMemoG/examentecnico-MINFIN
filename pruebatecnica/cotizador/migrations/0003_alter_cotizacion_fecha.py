# Generated by Django 5.1 on 2024-08-09 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizador', '0002_alter_cotizacion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2024, 8, 9, 16, 8, 5, 522866, tzinfo=datetime.timezone.utc)),
        ),
    ]

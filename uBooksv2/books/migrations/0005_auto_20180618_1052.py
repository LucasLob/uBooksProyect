# Generated by Django 2.0.6 on 2018-06-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_libro_creado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_equipmentlist_fileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentlist',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]

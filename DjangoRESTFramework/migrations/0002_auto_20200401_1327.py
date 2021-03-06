# Generated by Django 2.2.7 on 2020-04-01 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoRESTFramework', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapiinfo',
            name='resultsave',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='接口依赖数据'),
        ),
        migrations.AlterField(
            model_name='userapiinfo',
            name='url',
            field=models.URLField(max_length=1024, verbose_name='接口名称'),
        ),
    ]

# Generated by Django 2.2.7 on 2020-04-13 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoRESTFramework', '0009_auto_20200411_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapool',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_pool', to='DjangoRESTFramework.UserInfo', verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='userapiinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_api', to='DjangoRESTFramework.UserInfo', verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='userproject',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_project', to='DjangoRESTFramework.UserInfo', verbose_name='创建人'),
        ),
    ]

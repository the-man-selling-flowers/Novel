# Generated by Django 3.2.7 on 2021-09-27 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.category', verbose_name='カテゴリー'),
            preserve_default=False,
        ),
    ]

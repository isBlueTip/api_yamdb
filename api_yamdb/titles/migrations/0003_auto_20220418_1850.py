# Generated by Django 2.2.16 on 2022-04-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0002_auto_20220418_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(through='titles.Genre_title', to='titles.Genre'),
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
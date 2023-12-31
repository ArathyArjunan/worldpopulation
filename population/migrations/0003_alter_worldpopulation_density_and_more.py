# Generated by Django 4.2.7 on 2023-11-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('population', '0002_alter_worldpopulation_growthrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldpopulation',
            name='density',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='worldpopulation',
            name='densityMi',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='worldpopulation',
            name='growthRate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='worldpopulation',
            name='netChange',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='worldpopulation',
            name='worldPercentage',
            field=models.FloatField(),
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-07 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tariff',
            old_name='weight',
            new_name='max_weight',
        ),
        migrations.AddField(
            model_name='dimension',
            name='cube',
            field=models.FloatField(default=0.0, editable=False, help_text='Cube Dimension'),
        ),
        migrations.AddField(
            model_name='tariff',
            name='min_weight',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='dimension',
            name='height',
            field=models.FloatField(default=0.0, help_text='CM \nВысота / Balandlik'),
        ),
        migrations.AlterField(
            model_name='dimension',
            name='length',
            field=models.FloatField(default=0.0, help_text='CM \nДлина / Uzunlig'),
        ),
        migrations.AlterField(
            model_name='dimension',
            name='width',
            field=models.FloatField(default=0.0, help_text='CM \nШирина / Kenglik'),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='dimension',
            field=models.ForeignKey(help_text='Cubic meter: м3', on_delete=django.db.models.deletion.CASCADE, to='calc.dimension'),
        ),
    ]

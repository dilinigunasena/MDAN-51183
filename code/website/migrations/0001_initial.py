# Generated by Django 5.1 on 2024-08-20 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('model_number', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=25)),
                ('make', models.CharField(max_length=10)),
                ('yom', models.DateField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.0.5 on 2020-06-17 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('breed', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
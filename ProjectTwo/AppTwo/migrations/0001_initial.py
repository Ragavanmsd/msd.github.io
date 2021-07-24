# Generated by Django 3.2.5 on 2021-07-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=246)),
                ('lastName', models.CharField(max_length=246)),
                ('Email', models.EmailField(max_length=256, unique=True)),
            ],
        ),
    ]

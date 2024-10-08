# Generated by Django 4.2.15 on 2024-08-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-01 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='stream',
            name='category',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='channels/')),
                ('channel_number', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.category')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='games/')),
                ('description', models.TextField()),
                ('tags', models.ManyToManyField(blank=True, to='cinema.tag')),
                ('images', models.ManyToManyField(blank=True, to='cinema.image')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('poster', models.ImageField(upload_to='movies/')),
                ('release_date', models.DateField()),
                ('is_new', models.BooleanField(default=False)),
                ('is_popular', models.BooleanField(default=False)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.category')),
                ('images', models.ManyToManyField(blank=True, to='cinema.image')),
                ('tags', models.ManyToManyField(blank=True, to='cinema.tag')),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Stream',
        ),
    ]

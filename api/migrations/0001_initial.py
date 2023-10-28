# Generated by Django 4.2.6 on 2023-10-28 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='body')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
                'ordering': ['-updated'],
            },
        ),
    ]

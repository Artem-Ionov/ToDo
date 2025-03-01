# Generated by Django 5.1.4 on 2025-01-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Вопрос')),
                ('decision', models.TextField(blank=True, default='Пока не найдено', verbose_name='Решение')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['date']},
        ),
    ]

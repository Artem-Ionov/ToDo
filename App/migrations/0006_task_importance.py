# Generated by Django 5.1.4 on 2025-02-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_question_block_alter_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='importance',
            field=models.CharField(choices=[('о', 'Ерунда'), ('с', 'Средне')], default='с', max_length=1, verbose_name='Важность'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pulzion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=100, verbose_name='Question')),
                ('Option1', models.CharField(max_length=100, verbose_name='Option A')),
                ('Option2', models.CharField(max_length=100, verbose_name='Option B')),
                ('Option3', models.CharField(max_length=100, verbose_name='Option C')),
                ('Option4', models.CharField(max_length=100, verbose_name='Option D')),
                ('Optionans', models.CharField(max_length=100, verbose_name='Answer Option')),
            ],
        ),
    ]

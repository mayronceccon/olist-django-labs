# Generated by Django 3.0.3 on 2020-03-07 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula08', '0002_auto_20200307_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['ativo'], 'verbose_name': 'Animal', 'verbose_name_plural': 'Animais'},
        ),
        migrations.AlterField(
            model_name='pet',
            name='ativo',
            field=models.BooleanField(default=True, help_text='Pet ativo na plataforma'),
        ),
    ]

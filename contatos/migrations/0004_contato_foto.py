# Generated by Django 3.2 on 2021-05-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_rename_mostar_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/Y/%m/%d'),
        ),
    ]

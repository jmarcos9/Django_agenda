# Generated by Django 3.2 on 2021-05-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0005_alter_contato_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto2',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='contato',
            name='foto3',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='contato',
            name='foto4',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]

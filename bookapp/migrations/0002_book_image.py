# Generated by Django 4.2.14 on 2024-07-28 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1234, upload_to='book_media'),
            preserve_default=False,
        ),
    ]

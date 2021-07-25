# Generated by Django 3.2.5 on 2021-07-21 05:44

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libr', '0002_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookPDF',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='libr/'), upload_to='static/libr/pdf'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='libr/'), upload_to='static/libr/pictures'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=15)),
                ('favorites', models.ManyToManyField(to='libr.Book')),
            ],
        ),
    ]

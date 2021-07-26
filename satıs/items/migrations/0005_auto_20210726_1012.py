# Generated by Django 3.1.5 on 2021-07-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20210724_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='indirimli_fiyat',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='indirimsiz_fiyat',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='fiyat',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='lezzeti',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='üretim_tarihi',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='üretim_yeri',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

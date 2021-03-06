# Generated by Django 2.2.7 on 2019-12-18 05:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('parent_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
                ('state_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datacode.State')),
            ],
        ),
        migrations.CreateModel(
            name='Biz',
            fields=[
                ('biz_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('primary_contact', models.IntegerField()),
                ('secondary_contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('logo', models.ImageField(upload_to='biz/')),
                ('website', models.URLField()),
                ('estd_year', models.CharField(choices=[('2019', '2019'), ('2018', '2018')], max_length=200)),
                ('doc', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datacode.Category')),
            ],
        ),
    ]

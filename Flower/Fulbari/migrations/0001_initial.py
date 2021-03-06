# Generated by Django 4.0 on 2022-01-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('confirm_password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'customer_tbl',
            },
        ),
    ]

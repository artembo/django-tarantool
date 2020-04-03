# Generated by Django 3.0.4 on 2020-04-03 20:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigInteger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_integer', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Binary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binary', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Boolean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean', models.BooleanField(default=False, verbose_name='Bool value')),
            ],
        ),
        migrations.CreateModel(
            name='Char',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('date_time_auto', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Decimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decimal', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FilePath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepath', models.FilePathField(path='/Users/artem.morozov/projects/django-tarantool')),
            ],
        ),
        migrations.CreateModel(
            name='Float',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('float', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ForeignKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GenericIPAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address_v4', models.GenericIPAddressField(protocol='ipv4')),
                ('ip_address_v6', models.GenericIPAddressField(protocol='ipv6')),
                ('generic_ip_address', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='Integer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NullBoolean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('null_boolean', models.NullBooleanField(verbose_name='Null bool value')),
            ],
        ),
        migrations.CreateModel(
            name='OneToOneRelative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PositiveInteger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_integer', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PositiveSmallInteger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_small_integer', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Slug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='SmallInteger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_integer', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Uuid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='OneToOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_to_one', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='one', to='app.OneToOneRelative')),
            ],
        ),
        migrations.CreateModel(
            name='ManyToMany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('m2m', models.ManyToManyField(null=True, to='app.ForeignKey')),
            ],
        ),
        migrations.AddField(
            model_name='foreignkey',
            name='foreign_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Integer'),
        ),
        migrations.CreateModel(
            name='AllModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean', models.BooleanField(default=True)),
                ('char', models.CharField(max_length=1)),
                ('decimal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('file', models.FileField(upload_to='')),
                ('filepath', models.FilePathField(path='/Users/artem.morozov/projects/django-tarantool')),
                ('float', models.FloatField(null=True)),
                ('integer', models.IntegerField(null=True)),
                ('big_integer', models.BigIntegerField(null=True)),
                ('generic_ip_address', models.GenericIPAddressField()),
                ('null_boolean', models.NullBooleanField()),
                ('positive_integer', models.PositiveIntegerField()),
                ('positive_small_integer', models.PositiveSmallIntegerField()),
                ('slug', models.SlugField()),
                ('small_integer', models.SmallIntegerField()),
                ('text', models.TextField(null=True)),
                ('time', models.TimeField()),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('fk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='all_models', to='app.Integer')),
                ('one_to_one', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='all_model', to='app.Integer')),
            ],
        ),
    ]

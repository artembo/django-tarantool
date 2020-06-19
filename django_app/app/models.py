import uuid as uuid
from django.conf import settings
from django.db import models


class Boolean(models.Model):
    boolean = models.BooleanField('Bool value', default=False)

    def __str__(self): return str(self.boolean)


class NullBoolean(models.Model):
    null_boolean = models.NullBooleanField('Null bool value')

    def __str__(self): return str(self.null_boolean)


class File(models.Model):
    file = models.FileField()

    def __str__(self): return self.file.path if self.file else None


class FilePath(models.Model):
    filepath = models.FilePathField(path=settings.BASE_DIR)

    def __str__(self): return self.filepath


class Float(models.Model):
    float = models.FloatField()

    def __str__(self): return str(self.float)


class Decimal(models.Model):
    decimal = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self): return str(self.decimal)


class Integer(models.Model):
    integer = models.IntegerField()

    def __str__(self): return str(self.integer)


class BigInteger(models.Model):
    big_integer = models.BigIntegerField()

    def __str__(self): return str(self.big_integer)


class PositiveInteger(models.Model):
    positive_integer = models.PositiveIntegerField()

    def __str__(self): return str(self.positive_integer)


class SmallInteger(models.Model):
    small_integer = models.SmallIntegerField()

    def __str__(self): return str(self.small_integer)


class PositiveSmallInteger(models.Model):
    positive_small_integer = models.PositiveSmallIntegerField()

    def __str__(self): return str(self.positive_small_integer)


class OneToOneRelative(models.Model):

    def __str__(self): return str(self.pk)


class OneToOne(models.Model):
    one_to_one = models.OneToOneField(OneToOneRelative, models.CASCADE, related_name='one')

    def __str__(self): return str(self.pk)


class ForeignKey(models.Model):
    foreign_key = models.ForeignKey('app.Integer', on_delete=models.CASCADE)

    def __str__(self): return str(self.pk)


class M2MDependency(models.Model):
    pass


# Required "ALTER TABLE 'table_name' ADD COLUMN" which is not working in 2.3
# Used workaround from sqlite3 backend
class ManyToMany(models.Model):
    m2m = models.ManyToManyField('app.M2MDependency', blank=True)
    name = models.CharField(max_length=20)

    def __str__(self): return self.name


class GenericIPAddress(models.Model):
    ip_address_v4 = models.GenericIPAddressField(protocol='ipv4')
    ip_address_v6 = models.GenericIPAddressField(protocol='ipv6')
    generic_ip_address = models.GenericIPAddressField()

    def __str__(self): return self.generic_ip_address


class Char(models.Model):
    char = models.CharField(max_length=100)

    def __str__(self): return self.char


class Text(models.Model):
    text = models.TextField()

    def __str__(self): return self.text[:50]


class Uuid(models.Model):
    uuid = models.UUIDField()

    def __str__(self): return str(self.uuid)


class Slug(models.Model):
    slug = models.SlugField()

    def __str__(self): return self.slug


class DateTime(models.Model):
    date_time = models.DateTimeField(null=True, blank=True)
    date_time_auto = models.DateTimeField(auto_now_add=True)

    def __str__(self): return str(self.date_time)


class Date(models.Model):
    date = models.DateField()

    def __str__(self): return str(self.date)


class Time(models.Model):
    time = models.TimeField()

    def __str__(self): return str(self.time)


class Duration(models.Model):
    duration = models.DurationField()

    def __str__(self): return str(self.duration)


class Binary(models.Model):
    binary = models.BinaryField()

    def __str__(self): return str(self.pk)


class AllModel(models.Model):
    boolean = models.BooleanField(default=True)
    char = models.CharField(max_length=1)
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    file = models.FileField()
    filepath = models.FilePathField(path=settings.BASE_DIR)
    float = models.FloatField(null=True)
    integer = models.IntegerField(null=True)
    big_integer = models.BigIntegerField(null=True)
    generic_ip_address = models.GenericIPAddressField()
    null_boolean = models.NullBooleanField()
    one_to_one = models.OneToOneField('app.Integer', models.CASCADE, related_name='all_model')
    fk = models.OneToOneField('app.Integer', models.CASCADE, related_name='all_models')
    positive_integer = models.PositiveIntegerField()
    positive_small_integer = models.PositiveSmallIntegerField()
    slug = models.SlugField()
    small_integer = models.SmallIntegerField()
    text = models.TextField(null=True)
    time = models.TimeField()
    uuid = models.UUIDField(default=uuid.uuid4)

from django.db import models


class Boolean(models.Model):
    boolean = models.BooleanField('Bool value', default=False)
    def __str__(self): return str(self.boolean)


class NullBoolean(models.Model):
    null_boolean = models.NullBooleanField('Null bool value')
    def __str__(self): return str(self.null_boolean)


class Binary(models.Model):
    binary = models.BinaryField()


class File(models.Model):
    file = models.FileField()


class FilePath(models.Model):
    filepath = models.FilePathField()


class Float(models.Model):
    float = models.FloatField()
    def __str__(self): return str(self.float)


class Decimal(models.Model):
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self): return str(self.decimal)


class Integer(models.Model):  # Manually tested
    integer = models.IntegerField()
    def __str__(self): return str(self.integer)


class BigInteger(models.Model):  # Manually tested
    big_integer = models.BigIntegerField()
    def __str__(self): return str(self.big_integer)


class PositiveInteger(models.Model):  # Manually tested
    positive_integer = models.PositiveIntegerField()
    def __str__(self): return str(self.positive_integer)


class SmallInteger(models.Model):  # Manually tested
    small_ineger = models.SmallIntegerField()
    def __str__(self): return str(self.small_ineger)


class PositiveSmallInteger(models.Model):  # Manually tested
    positive_small_integer = models.PositiveSmallIntegerField()
    def __str__(self): return str(self.positive_small_integer)


class OneToOneRelative(models.Model):
    def __str__(self): return str(self.pk)


class OneToOne(models.Model):
    one_to_one = models.OneToOneField(OneToOneRelative, models.CASCADE, related_name='one')


class GenericIPAddress(models.Model):
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


class AllModel(models.Model):

    binary = models.BinaryField(null=True)
    boolean = models.BooleanField(default=True)
    char = models.CharField(max_length=1)
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    file = models.FileField()
    filepath = models.FilePathField()
    float = models.FloatField(null=True)
    integer = models.IntegerField(null=True)
    big_integer = models.BigIntegerField(null=True)
    generic_ip_address = models.GenericIPAddressField()
    null_boolean = models.NullBooleanField()
    one_to_one = models.OneToOneField('self', models.CASCADE, related_name='all_model')
    fk = models.OneToOneField('self', models.CASCADE, related_name='all_models')
    positive_integer = models.PositiveIntegerField()
    positive_small_integer = models.PositiveSmallIntegerField()
    slug = models.SlugField()
    small_integer = models.SmallIntegerField()
    text = models.TextField(null=True)
    time = models.TimeField()
    uuid = models.UUIDField()

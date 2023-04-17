from django.db import models


# Create your models here.
class userInfo(models.Model):
    ip = models.CharField(max_length=20)
    ipType = models.CharField(max_length=10)
    contCode = models.CharField(max_length=10)
    contName = models.CharField(max_length=30)
    countryCode = models.CharField(max_length=10)
    countryName = models.CharField(max_length=30)
    regCode = models.CharField(max_length=10)
    regName = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    zip = models.CharField(max_length=10)


class weatherData(models.Model):
    location = models.CharField(max_length=30)
    region = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    timezone = models.CharField(max_length=30)
    localt = models.CharField(max_length=30)
    lat = models.CharField(max_length=10)
    lon = models.CharField(max_length=10)


class airQuality(models.Model):
    carbon = models.CharField(max_length=30)
    nox = models.CharField(max_length=30)
    o3 = models.CharField(max_length=30)
    so2 = models.CharField(max_length=30)
    fine = models.CharField(max_length=30)
    ultra = models.CharField(max_length=30)
    usa = models.CharField(max_length=5)
    eu = models.CharField(max_length=5)


class temp(models.Model):
    tempc = models.CharField(max_length=5)
    tempf = models.CharField(max_length=5)
    hum = models.CharField(max_length=5)
    flc = models.CharField(max_length=5)
    flf = models.CharField(max_length=5)
    wskm = models.CharField(max_length=10)
    wsm = models.CharField(max_length=10)
    wd = models.CharField(max_length=5)
    wdd = models.CharField(max_length=5)
    epmm = models.CharField(max_length=5)
    epin = models.CharField(max_length=5)


class general(models.Model):
    lst = models.CharField(max_length=30)
    tod = models.CharField(max_length=20)
    cloud = models.CharField(max_length=5)
    cond = models.ImageField()
    uv = models.CharField(max_length=5)
    vkm = models.CharField(max_length=5)
    vm = models.CharField(max_length=5)
    pmb = models.CharField(max_length=10)
    piw = models.CharField(max_length=10)

from django.db import models

class UserInfo(models.Model):
    uname =models.CharField(max_length=10)
    upwd =models.CharField(max_length=40)
    isDelete =models.BooleanField()


class BookInfo(models.Model):
    btitle =models.CharField(max_length=20)
    bpub_date =models.DateField(db_column='pub_date')
    bread =models.IntegerField(default=0)
    bcommet =models.IntegerField(default=0)
    isDelete =models.BooleanField(default=0)

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey(BookInfo)


class AreaInfo(models.Model):
    title=models.CharField(max_length=20)
    parea=models.ForeignKey('self',null=True,blank=True)
from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=50)
    Monday_time = models.BigIntegerField(default=0,blank=True)
    Tuesday_time = models.BigIntegerField(default=0,blank=True)
    Wednesday_time = models.BigIntegerField(default=0,blank=True)
    thirsday_time = models.BigIntegerField(default=0,blank=True)
    Friday_time = models.BigIntegerField(default=0,blank=True)
    Saturday_time = models.BigIntegerField(default=0,blank=True)
    Sunday_time = models.BigIntegerField(default=0,blank=True)
    total_time = models.BigIntegerField(default=0,blank=True)
    status = models.IntegerField(default=0,blank=True)

    date_match_dict = {"Monday":Monday_time,
                   "Tuesday":Tuesday_time,
                   "Wednesday":Wednesday_time,
                   "Thirsday":thirsday_time,
                   "Friday":Friday_time,
                   "Saturday":Saturday_time,
                   "Sunday":Sunday_time,
                   }

    def __unicode__(self):
        return self.name

from django.db import models

# Create your models here.

class Posts(models.Model):
    class ChargeType(models.TextChoices):
        walk_in="Walk In Drive"
        Offline="OFLINE"
        Online= "ONLINE"
    company_name= models.CharField(max_length=300)
    job_title = models.CharField(max_length=256, blank=True, null=True)
    year_passing = models.CharField(max_length=50)
    hiring_process= models.CharField(max_length=50,choices=ChargeType.choices)
    contact_number = models.CharField(max_length=15)
    job_discription= models.TextField(blank=True, null=True)
    eligibility= models.TextField(blank=True, null=True)
    qualification = models.TextField(blank=True, null=True)
    experience = models.IntegerField(default=0)  # in years
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=50)
    offical_site = models.TextField(blank=True, null=True)

    apply_link= models.TextField(blank=True, null=True)
    more_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.job_title
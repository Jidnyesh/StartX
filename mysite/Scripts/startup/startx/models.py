from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.ImageField(null=True)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,null=True)
    price = models.IntegerField(default=0)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    patient_number = models.IntegerField(default=0)
    product_category = models.CharField(max_length=30,null=True)
    likes = models.ManyToManyField(User,related_name="products",null=True)


    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.TextField()
    company_name = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.description
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Job(models.Model):
    job_title = models.CharField(max_length=100,null = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    job_description = models.TextField(max_length=1000,null = True)
    category = models.CharField(max_length=50,null = True)
    requirements = models.TextField(max_length=2000,null=True)
    required_skills = models.TextField(max_length=2000,null=True)
    income = models.IntegerField(default=0,null = True)
    project_number = models.IntegerField(default=0,null = True)
    time = models.DateTimeField(auto_now=False,auto_now_add=True,null = True)
    location = models.CharField(max_length=100,null = True)

    def __str__(self):
        return self.job_title


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Comments(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="products")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text

class Advertisement(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    category = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    duration = models.IntegerField(default=5)
    contact_number = models.IntegerField(default=0)
    city = models.CharField(max_length=40,null=True)
    location = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title

from django.db import models


class User(models.Model):
    phone = models.CharField(max_length=13, primary_key=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=50)
    pic = models.FileField(max_length=100, upload_to='Userpics/')
    email = models.CharField(max_length=50)
    address = models.TextField()


class Company(models.Model):
    CHOICES = (
        ('Car', 'Car'), 
        ('Bike', 'Bike'),
    )
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    pic = models.FileField(max_length=100, upload_to='Companies/')
    rating = models.CharField(max_length=10, default="★★★★★")
    description = models.TextField(null=True)
    type_of_vehicle = models.CharField(max_length=50, choices=CHOICES)




class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    vehicle_img = models.FileField(max_length=100, upload_to='Vehicles/', default="")
    vehicle_company = models.CharField(max_length=100, default="")
    vehicle_name = models.CharField(max_length=100, default="")
    vehicle_number = models.CharField(max_length=100, default="")
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']




class Feedback(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.DO_NOTHING)
    rating = models.CharField(max_length=10, default="★★★★★")
    remark = models.TextField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        
class AdminMod(models.Model):
    aid = models.CharField(max_length=100)
    ad = models.BooleanField(default=True)
    password = models.CharField(max_length=100)
    name= models.CharField(max_length=20, default="Admin")
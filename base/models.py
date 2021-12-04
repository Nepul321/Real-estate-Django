from django.db import models
from django.contrib.auth.models import User

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='realtor_pics/%Y/%m/%d/')
    description = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Realtor " + str(self.id)

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    main_photo = models.ImageField(upload_to="main-photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Inquiry(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, unique=True)
    message = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Inquiry " + str(self.id)


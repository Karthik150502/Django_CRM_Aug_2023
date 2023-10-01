from django.db import models
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    name =  models.CharField(max_length = 200)
    ceo = models.CharField(max_length = 200)
    origin = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("card_app:detail", kwargs = {"pk":self.pk})


class Products(models.Model):

    product_name = models.CharField(max_length = 200)
    mileage = models.IntegerField()
    cc = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length = 200)
    year = models.IntegerField()
    company = models.ForeignKey(Company, related_name = "companies", on_delete = models.CASCADE)

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse("card_app:p_detail", kwargs = {"pk":self.company_details.pk})

    
    # def get_absolute_url(self):
    #     return reverse("card_app:detail", kwargs = {"pk":self.pk})
from django.db import models

# class Cartype(models.Model):
#     title = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
#
# class Country(models.Model):
#     title = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title
#
# class Car(models.Model):
#     title = models.CharField(max_length=100)
#     model = models.ForeignKey(Cartype, on_delete=models.CASCADE, related_name="models")
#     country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="countries")
#     colour = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
#
#     def __str__(self):
#         return self.title


class Cartype(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "CARtype"
        verbose_name_plural = "CARtypes"
        ordering = ['title']

class Country(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "COUNTRY"
        verbose_name_plural = "COUNTRIES"
        ordering = ['title']

class Car(models.Model):
    title = models.CharField(max_length=100)
    model = models.ForeignKey(Cartype, on_delete=models.CASCADE, related_name="models")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="countries")
    colour = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "CAR"
        verbose_name_plural = "CARS"
        ordering = ['title']
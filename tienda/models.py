from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        db_table = "category"
    
    def __str__(self):
        return self.name
    
    def capitalized_name(self):
        return self.name.capitalize()

class Product(models.Model):
    name = models.CharField(max_length=200)
    url_image = models.ImageField(upload_to = "products")
    price = models.FloatField()
    discount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, db_column="category")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "proyectos"
        ordering = ["category"]
        db_table = "product"

    def __str__(self):
        return self.name
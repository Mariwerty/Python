from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return f"{self.title}: {self.created_by.get_full_name()}"

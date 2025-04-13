from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    description = models.TextField(blank=True, null=True, verbose_name="Опис категорії")
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True, verbose_name="Іконка категорії")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ['name']

class Product(models.Model):
    STATUS_CHOICES = [
        ('available', 'В наявності'),
        ('out_of_stock', 'Немає в наявності'),
        ('coming_soon', 'Скоро у продажу'),
        ('discontinued', 'Знято з виробництва'),
    ]
    
    SIZE_CHOICES = [
        ('S', 'Маленький'),
        ('M', 'Середній'),
        ('L', 'Великий'),
        ('XL', 'Дуже великий'),
    ]
    
    # Обов'язкові поля
    name = models.CharField(max_length=200, verbose_name="Назва товару")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категорія")
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], verbose_name="Ціна")
    
    # Поля з default значеннями
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість на складі")
    is_featured = models.BooleanField(default=False, verbose_name="Рекомендований товар")
    discount_percentage = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], verbose_name="Відсоток знижки")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="Статус")
    
    # Поля з різними опціями
    description = models.TextField(blank=True, null=True, verbose_name="Опис товару")
    specifications = models.JSONField(blank=True, null=True, verbose_name="Характеристики")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name="Зображення товару")
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, blank=True, null=True, verbose_name="Розмір")
    weight = models.FloatField(blank=True, null=True, help_text="Вага товару в кілограмах", verbose_name="Вага")
    
    # Службові поля
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    
    def get_discounted_price(self):
        if self.discount_percentage > 0:
            return round(self.price * (1 - self.discount_percentage / 100), 2)
        return self.price
    
    def is_new(self):
        return (timezone.now() - self.created_at).days < 30
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ['-created_at']
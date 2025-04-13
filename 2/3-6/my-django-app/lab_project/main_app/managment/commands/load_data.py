from django.core.management.base import BaseCommand
from main_app.models import Category, Product
import json

class Command(BaseCommand):
    help = 'Додає початкові дані для магазину Soma-Dogs'

    def handle(self, *args, **kwargs):
        # Створюємо категорії
        categories = [
            {
                'name': 'Корми',
                'description': 'Сухі та вологі корми для собак різних порід та віку',
                'is_active': True
            },
            {
                'name': 'Аксесуари',
                'description': 'Нашийники, повідки, намордники та інші аксесуари для собак',
                'is_active': True
            },
            {
                'name': 'Іграшки',
                'description': 'Розвиваючі та звичайні іграшки для собак',
                'is_active': True
            },
            {
                'name': 'Одяг',
                'description': 'Одяг для собак різних розмірів',
                'is_active': True
            },
        ]
        
        # Створюємо категорії та зберігаємо їх ідентифікатори
        category_ids = {}
        for category_data in categories:
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults=category_data
            )
            category_ids[category_data['name']] = category.id
            status = 'створено' if created else 'вже існує'
            self.stdout.write(f"Категорія '{category.name}' {status}")
        
        # Створюємо товари
        products = [
            {
                'name': 'Royal Canin Medium Adult',
                'category': category_ids['Корми'],
                'price': 799.99,
                'stock_quantity': 25,
                'is_featured': True,
                'discount_percentage': 5,
                'status': 'available',
                'description': 'Сухий корм для дорослих собак середніх порід від 12 місяців до 7 років',
                'specifications': json.dumps({
                    'вага': '4 кг',
                    'для_віку': 'дорослі',
                    'для_породи': 'середня',
                    'тип': 'сухий'
                }),
                'size': 'M',
                'weight': 4.0
            },
            {
                'name': 'Ласощі для тренування Pedigree',
                'category': category_ids['Корми'],
                'price': 89.99,
                'stock_quantity': 50,
                'is_featured': False,
                'discount_percentage': 0,
                'status': 'available',
                'description': 'Ласощі для тренування собак усіх порід',
                'specifications': json.dumps({
                    'вага': '0.2 кг',
                    'для_віку': 'всі',
                    'для_породи': 'всі',
                    'тип': 'ласощі'
                }),
                'size': 'S',
                'weight': 0.2
            },
            {
                'name': 'Нашийник шкіряний преміум',
                'category': category_ids['Аксесуари'],
                'price': 499.99,
                'stock_quantity': 10,
                'is_featured': True,
                'discount_percentage': 0,
                'status': 'available',
                'description': 'Шкіряний нашийник ручної роботи з металевими вставками',
                'specifications': json.dumps({
                    'матеріал': 'натуральна шкіра',
                    'для_розміру': 'великі породи',
                    'колір': 'коричневий',
                    'довжина': '40-50 см'
                }),
                'size': 'L',
                'weight': 0.15
            },
            {
                'name': 'М\'яч для собак Kong',
                'category': category_ids['Іграшки'],
                'price': 199.99,
                'stock_quantity': 30,
                'is_featured': True,
                'discount_percentage': 10,
                'status': 'available',
                'description': 'Міцний гумовий м\'яч для активних ігор',
                'specifications': json.dumps({
                    'матеріал': 'гума',
                    'для_розміру': 'всі породи',
                    'колір': 'червоний',
                    'діаметр': '7 см'
                }),
                'size': 'M',
                'weight': 0.1
            },
            {
                'name': 'Жилет зимовий для собак',
                'category': category_ids['Одяг'],
                'price': 349.99,
                'stock_quantity': 15,
                'is_featured': False,
                'discount_percentage': 0,
                'status': 'available',
                'description': 'Теплий зимовий жилет для собак з водовідштовхуючим покриттям',
                'specifications': json.dumps({
                    'матеріал': 'нейлон, фліс',
                    'для_розміру': 'малі та середні породи',
                    'колір': 'синій',
                    'сезон': 'зима'
                }),
                'size': 'S',
                'weight': 0.25
            },
            {
                'name': 'Повідець-рулетка Flexi',
                'category': category_ids['Аксесуари'],
                'price': 399.99,
                'stock_quantity': 20,
                'is_featured': False,
                'discount_percentage': 15,
                'status': 'available',
                'description': 'Повідець-рулетка з стрічкою довжиною до 5 метрів',
                'specifications': json.dumps({
                    'матеріал': 'пластик, нейлон',
                    'для_розміру': 'малі та середні породи',
                    'колір': 'чорний',
                    'довжина': '5 м'
                }),
                'size': 'M',
                'weight': 0.3
            },
            {
                'name': 'Іграшка-пищалка курча',
                'category': category_ids['Іграшки'],
                'price': 99.99,
                'stock_quantity': 40,
                'is_featured': False,
                'discount_percentage': 0,
                'status': 'available',
                'description': 'М\'яка іграшка з пищалкою у формі курчати',
                'specifications': json.dumps({
                    'матеріал': 'плюш, пластик',
                    'для_розміру': 'всі породи',
                    'колір': 'жовтий',
                    'тип': 'пищалка'
                }),
                'size': 'S',
                'weight': 0.05
            },
            {
                'name': 'Дощовик для собак',
                'category': category_ids['Одяг'],
                'price': 259.99,
                'stock_quantity': 18,
                'is_featured': False,
                'discount_percentage': 5,
                'status': 'available',
                'description': 'Легкий дощовик з капюшоном для захисту від дощу',
                'specifications': json.dumps({
                    'матеріал': 'поліестер',
                    'для_розміру': 'малі та середні породи',
                    'колір': 'жовтий',
                    'сезон': 'весна-осінь'
                }),
                'size': 'M',
                'weight': 0.15
            },
            {
                'name': 'Щітка для вичісування шерсті',
                'category': category_ids['Аксесуари'],
                'price': 159.99,
                'stock_quantity': 25,
                'is_featured': False,
                'discount_percentage': 0,
                'status': 'available',
                'description': 'Професійна щітка для вичісування шерсті собак',
                'specifications': json.dumps({
                    'матеріал': 'метал, пластик',
                    'для_шерсті': 'коротка та середня',
                    'колір': 'синій',
                    'тип': 'фурмінатор'
                }),
                'size': None,
                'weight': 0.12
            },
            {
                'name': 'Ультразвуковий свисток для тренування',
                'category': category_ids['Аксесуари'],
                'price': 129.99,
                'stock_quantity': 15,
                'is_featured': False,
                'discount_percentage': 0,
                'status': 'available',
                'description': 'Ультразвуковий свисток для тренування собак з регульованою частотою',
                'specifications': json.dumps({
                    'матеріал': 'метал',
                    'частота': '15-25 кГц',
                    'колір': 'срібний',
                    'довжина': '7 см'
                }),
                'size': None,
                'weight': 0.03
            },
        ]
        
        # Додаємо товари
        products_added = 0
        for product_data in products:
            specifications = product_data.pop('specifications')
            product_data['specifications'] = json.loads(specifications)
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            products_added += 1 if created else 0
            
        self.stdout.write(self.style.SUCCESS(f'Додано {products_added} товарів'))
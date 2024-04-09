from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Запчасти', 'description': 'Колодки, диски и др.'},
            {'name': 'Тюнинг', 'description': 'Спойлера, зеркала и др.'},
            {'name': 'Аксессуары', 'description': 'Коврики, чехлы на ключ и др.'},
        ]

        category_for_create = []

        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'name': 'Коврики BMW G05', 'description': 'Резиновые коврики на BMW G05 с высоким бором',
             'pur_price': 15000.00, 'category': Category.objects.get(name='Аксессуары')},
            {'name': 'Чехол для ключа', 'description': 'Чехол для ключа на BMW G-серии', 'pur_price': 5000.00,
             'category': Category.objects.get(name='Аксессуары')},
            {'name': 'Колодки METACO', 'description': 'Супер дешевые колодки, лучше ездить без тормозов',
             'pur_price': 500.00, 'category': Category.objects.get(name='Запчасти')},
            {'name': 'Спойлер карбон BMW G16', 'description': 'Из настоящего карбона(не кованного)',
             'pur_price': 50000.00, 'category': Category.objects.get(name='Тюнинг')},
        ]

        product_for_create = []

        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_create)

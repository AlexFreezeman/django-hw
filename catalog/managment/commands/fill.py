from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = [{'title': 'Игровые консоли'}, {'title': 'Наушники'}, {'title': 'Мышки'}, {'title': 'Колонки'}]

        Category.objects.all().delete()

        categories_to_create = []
        for category_item in categories:
            categories_to_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_to_create)

        products = [{'title': 'Sony Playstation 5', 'price': 500, 'category': categories_to_create[0]},
                    {'title': 'Steelseries Arctis 1', 'price': 60, 'category': categories_to_create[1]},
                    {'title': 'Razer DeathAdder V2', 'price': 50, 'category': categories_to_create[2]},
                    {'title': 'Колонки 2.0 Edifier', 'price': 350, 'category': categories_to_create[3]}]

        Product.objects.all().delete()

        products_to_create = []
        for product_item in products:
            products_to_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_to_create)

        print("Готово")
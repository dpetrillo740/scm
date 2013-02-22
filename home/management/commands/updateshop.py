from django.core.management.base import BaseCommand, CommandError
from home.models import Sku
import shopify
from shopifyapp.decorators import shop_login_required

class Command(BaseCommand):
    args = 'none specified'
    help = 'Updates the local db from the external shopify API'

    @shop_login_required
    def handle(self, *args, **options):
        products = shopify.Product.find(limit=50)
        for product in products:
            if product.attributes['published_at']:
                for variant in product.attributes['variants']:
                    sku = Sku(sku=variant.sku, title=product.attributes['title'], variant=variant.title)
                    sku.save()
        self.stdout.write('Successfully updated the local DB')
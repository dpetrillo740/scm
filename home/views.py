from django.shortcuts import render_to_response
from django.template import RequestContext
import shopify
from shopifyapp.decorators import shop_login_required

def welcome(request):
    return render_to_response('home/welcome.html', {
        'callback_url': "http://%s/login/finalize" % (request.get_host()),
    }, context_instance=RequestContext(request))

@shop_login_required
def index(request):
    products = shopify.Product.find(limit=50)
    active_products = []
    for product in products:
        if product.attributes['published_at']:
            active_products.append(product)
            
    orders = shopify.Order.find(limit=10, status='any', fulfillment_status='unshipped', order="created_at DESC")
    return render_to_response('home/index.html', {
        'products': active_products,
        'orders': orders,
    }, context_instance=RequestContext(request))

def design(request):
    return render_to_response('home/design.html', {},
                              context_instance=RequestContext(request))

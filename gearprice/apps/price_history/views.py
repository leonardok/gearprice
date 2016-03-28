import types
import json
import requests
import locale
from lxml import html
from datetime import date

from django.shortcuts import render
from django.http import HttpResponse

from gearprice.apps.price_history.models import Gear, PriceHistory, Brand


def get_item_by_xpath(url, xpath):
        page = requests.get(url)
        tree = html.fromstring(page.text)
        price = tree.xpath(xpath + '/text()')

        if isinstance(price, types.ListType):
            price = price[0]

        return price


def xpath_tester(request, *args, **kwargs):
    price = None

    if request.method == 'POST':
        url = request.POST.get('url')
        xpath = request.POST.get('xpath')

        price = get_item_by_xpath(url, xpath)

    return render(request, 'xpath_tester.html', {'price': price})


def get_prices(request):
    updated = []
    errors = []
    response_data = {}

    page = 0
    limit = 10

    if request.method != 'GET':
        return render(request, 'update.html', {'updated': "", 'errors': ""})

    total_gears = Gear.objects.count()
        
    if request.GET.get('page'):
        page = request.GET.get('page')

    if request.GET.get('limit'):
        limit = request.GET.get('limit')

    offset = int(limit) * int(page)

    if(offset > total_gears):
        response_data['erors'] = 'page not found at offset %d' % offset
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    gears = Gear.objects.order_by('name')[offset:limit+offset]

    for gear in gears:
        urls = gear.url_set.all()

        for url in urls:
            price = None

            try:
                price_s = get_item_by_xpath(url.url, url.store.xpath)
            except Exception, e:
                errors.append("Gear: %s - Error: %s" % (gear.name, e))

                # get out of this one
                continue

            locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
            price = locale.atof(price_s.strip("$"))

            today = date.today()

            (ph, created) = PriceHistory.objects.get_or_create(gear=gear, date=today)

            print "Update conditions -- price:%s; new price:%s and created:%s" % (ph.price, price, created)

            if (ph.price is None and price is not None) or (float(ph.price) > float(price)):
                ph.price = price
                ph.store_name = url.store.name
                ph.save()

                print "Updated %s: %s" % (gear.name, str(ph))

                updated.append(gear.name)

    response_data['total'] = total_gears
    response_data['errors'] = errors
    response_data['updated'] = updated
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def index(request):
    brands = []

    brands = Brand.objects.order_by('name')
    return render(request, 'index.html', {'brands': brands})


def show(request, gear_id):
    gear = Gear.objects.get(id=gear_id)
    brands = Brand.objects.order_by('name')

    graph_items = []
    price_history = gear.pricehistory_set.order_by('date')
    for price in price_history:
        graph_items.append('{"x": "%s", "y": %s}' % (price.date, price.price))

    return render(request, 'show.html', {'gear': gear, 'price_history': price_history,
                                         'brands': brands,
                                         'graph_data': ",".join(graph_items),
                                         'newest_price': price_history.last(),
                                         'oldest_price': price_history.first() })



def content_partial(request, gear_id):
    gear = Gear.objects.get(id=gear_id)

    graph_items = []
    price_history = gear.pricehistory_set.order_by('date')
    for price in price_history:
        graph_items.append('{"x": "%s", "y": %s}' % (price.date, price.price))

    return render(request, '_show_content.html', {'gear': gear, 'price_history': price_history,
                                         'graph_data': ",".join(graph_items),
                                         'newest_price': price_history.last(),
                                         'oldest_price': price_history.first() })




def new_alarm(request, gear_id):
    return

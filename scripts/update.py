#!/bin/python

import math
import requests

host = "http://www.gearprice.info/"
gears_url = host + "api/v1/gear/?format=json"
update_url = host + "update"

r = requests.get(gears_url)
total_count = r.json()['meta']['total_count']

pages = int(math.ceil(total_count/10.0))

print "Pages: %d -- Total Count of gear objects: %d\n" % (pages, total_count)

for page in range(pages):
    print "Updating page: %d" % page

    payload = {'page': page}
    r = requests.get(update_url, params=payload)

    print "Page (%s): %s" % (r.url, r.json())

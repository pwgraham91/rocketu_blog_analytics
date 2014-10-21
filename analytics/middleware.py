from ipware.ip import get_real_ip
import requests
from analytics.models import Page, Location, View
from rocketu_blog_analytics import settings

__author__ = 'GoldenGate'
class LocationMiddleware(object):
    def process_request(self, request):
        # Get the IP Address of this request
        ip = get_real_ip(request)

        # If we didn't get an IP Address and we're developing locally,
        # make an API call to get our IP Address.
        if ip is None and settings.DEBUG:
            ip = requests.get('http://icanhazip.com/').text
        print ip
        if ip is not None:
            response = requests.get('http://ipinfo.io/{}/json'.format(ip))
            if response.status_code == 200:
                request.location = response.json()
                # Split out the lat and long from the location
                request.location['latitude'], request.location['longitude'] = request.location['loc'].split(',')

        request.ip = ip
        print request.location['latitude']

class AnalyticsMiddleware(object):
    def process_request(self, request):
        # TODO get or create page object
        # TODO get or create location object
        # TODO get url to create page object
        spec_url = request.META['PATH_INFO']
        print spec_url
        request_page, created = Page.objects.get_or_create(url=spec_url)
        new_city = request.location['city']
        new_region = request.location['region']
        new_country = request.location['country']
        new_location, created = Location.objects.get_or_create(city=new_city, region=new_region, country=new_country)
        new_lat = request.location['latitude']
        new_lon = request.location['longitude']

        View.objects.get_or_create(latitude=new_lat, longitude=new_lon, page=request_page, location=new_location, ip_address=request.ip)

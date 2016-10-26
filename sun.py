import urllib.request
import json
import datetime
from dateutil import parser, tz

class Sun(object):
    """docstring for Sun.
    Uses sunrise-sunset.org API to find time of Sunrise and Sunset
    returns both times as datetime objects"""
    def __init__(self):
        super(Sun, self).__init__()
        self.BASE_URL = "http://api.sunrise-sunset.org/json?lat=-37.8481330&lng=145.0092150&date=today&formatted=0"

    def request(self):
        return urllib.request.urlopen(self.BASE_URL).read().decode("utf-8")

    def update_times(self):
        to_zone = tz.gettz('Australia/Melbourne')
        data = json.loads(self.request())
        sunrise = data["results"]["sunrise"]
        sunrise_obj = parser.parse(sunrise)
        sunrise_obj_local = sunrise_obj.astimezone(to_zone)
        sunset = data["results"]["sunset"]
        sunset_obj = parser.parse(sunset)
        sunset_obj_local = sunset_obj.astimezone(to_zone)
        return (sunrise_obj_local, sunset_obj_local)

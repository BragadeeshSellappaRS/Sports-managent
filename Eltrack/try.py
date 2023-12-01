from flask import Flask, render_template, request
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

import phonenumbers 
import phonenumbers.carrier 

num_object = None 

while num_object is None: 
    try: 
        phone_number ="+919842209175"
        num_object = phonenumbers.parse("+1 {}".format(phone_number)) 
    except Exception as error: 
        print("ERROR: {}".format(error)) 
          



#country
locate = geocoder.description_for_number(num_object,'en')
print(locate)
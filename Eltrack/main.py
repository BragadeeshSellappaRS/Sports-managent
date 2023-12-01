from flask import Flask, render_template, request
import phonenumbers
import opencage
import folium
from phonenumbers import geocoder as gc
from geopy.geocoders import Nominatim
from opencage.geocoder import OpenCageGeocode


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/phone_form', methods=['GET', 'POST'])
def phone_form():
    if request.method == 'POST':
        phone_number = request.form['phone']
        num_object = phonenumbers.parse(phone_number) 
        #country
        locate = gc.description_for_number(num_object,'en')
        key = "35fe7e54863942898334ae1ccc9d1757"
        geocoder = OpenCageGeocode(key)
        query = str(locate)
        result = geocoder.geocode(query)
        lat  = result[0]['geometry']['lat']
        lng  = result[0]['geometry']['lng']
        print(lat,lng)
        myMap = folium.Map(location = [lat,lng],zoom_start=9)
        icon1 = folium.features.CustomIcon("templates/train.png", icon_size=(70,70))
        icon2 = folium.features.CustomIcon("templates/marker-shadow.png", icon_size=(100,100))
        folium.Marker([lat+.0028,lng+.0028],popup = locate,icon=icon1).add_to(myMap)
        folium.Marker([lat,lng],popup = locate,icon=icon2).add_to(myMap)
        myMap.save("templates/mylocation.html")
        return render_template("mylocation.html")
    return render_template('phone_form.html')

if __name__ == '__main__':
    app.run(debug=True)


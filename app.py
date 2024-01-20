# app.py
from flask import Flask, render_template, request
from opencage.geocoder import OpenCageGeocode

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

api_key = "YOUR_OPENCAGE_API_KEY"
geocoder = OpenCageGeocode(api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track_location():
    phone_number = request.form.get('phone_number')

    # Use the OpenCage Geocoding API to get location coordinates
    results = geocoder.geocode(phone_number)
    
    if results:
        latitude, longitude = results[0]['geometry']['lat'], results[0]['geometry']['lng']
        return render_template('map.html', latitude=latitude, longitude=longitude)
    else:
        return "Location not found."

if __name__ == '__main__':
    app.run(debug=True)

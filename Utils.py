import os
import json
import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, firestore
load_dotenv()

# Get the credentials from the environment variable
cred = credentials.Certificate({
    "type": os.getenv("FIREBASE_TYPE"),
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN")
})


# Create a credentials object from the dictionary

# Initialize the Firebase app with the credentials
firebase_admin.initialize_app(cred)
db = firestore.client()

def read_driver_trips(driver_id):
    # Reference to the 'trips' sub-collection of the specified driver
    trips_ref = db.collection('drivers').document(driver_id).collection('Trips')

    # Get all documents in the 'trips' sub-collection
    trips = trips_ref.get()

    # Check if there are any trips
    if trips:
        print(f'Trips for driver ID: {driver_id}')
        trip_list = []  # List to hold trip data
        for trip in trips:
            trip_list.append(trip.to_dict())  # Append each trip to the list
        return trip_list  # Return the list of trips
    else:
        print(f'No trips found for driver ID: {driver_id}.')
        return []  # Return an empty list if no trips found

def read_drivers():
    # Reference to the 'drivers' collection
    drivers_ref = db.collection('drivers')
    drivers = drivers_ref.get()

    driver_list = []  # List to hold driver data
    if drivers:
        for driver in drivers:
            driver_list.append(driver.to_dict())  # Append each driver to the list
        return driver_list  # Return the list of drivers
    else:
        print('No drivers found.')
        return []  # Return an empty list if no drivers found



import pandas as pd
import numpy as np
import os


if __name__ == '__main__':

    number_of_users = pd.read_csv('data/wifi_users_by_years.csv', delimiter=';', encoding='latin-1')
    wifi_locations = pd.read_csv('data/wifi_point_locations.csv', delimiter=',')
    kiosk_locations = pd.read_csv('data/kiosk_locations.csv', delimiter=',')
    parking_locations = pd.read_csv('data/parking_locations.csv', delimiter=',')


    print(number_of_users.head())


    location_group_english_to_turkish = {
        "Mobil": "Mobile",
        "Hizmet Binasi": "Service Building",
        "Diger": "Other",
        "Koyler": "Village",
        "Yesil Alan": "Green Area",
        "Tramvay Istasyonu": "Tram Station",
        "Spor Tesisi": "Sport Facility",
        "Kultur Merkezi": "Culture Center",
        "Metrobus Duragi": "Metrobus Station",
        "Sehir Hatlari Vapuru": "City Ferry",
        "Otobus Duragi": "Bus Station",
        "Sosyal Tesis": "Social Facility",
        "Kutuphane": "Library",
        "Ismek": "Teacher's House",
        "Turistik Mekan": "Tourist Place",
        "Sehir Hatlari Iskelesi": "City Ferry"
    }

    wifi_locations['LOCATION_GROUP'] = wifi_locations['LOCATION_GROUP'].replace(location_group_english_to_turkish,
                                                                             regex=True)

    wifi_locations.drop(columns=['LOCATION_TYPE', 'LOCATION_CODE', 'LOCATION'], inplace=True)
    print(wifi_locations.head())


    kiosk_locations.drop(columns=['Ilce_Adi', 'Mahalle_Adi', 'Bufe_Adi'], inplace=True)
    kiosk_locations.rename(columns={'Enlem': 'LATITUDE', 'Boylam': 'LONGITUDE'}, inplace=True)

    print(kiosk_locations.head())


    kiosk_locations.drop(columns=['PARK_NAME', 'LOCATION_NAME', 'PARK_TYPE_ID', 'PARK_TYPE_DESC', 'COUNTY_NAME'],
                         inplace=True)
    print(parking_locations.head())





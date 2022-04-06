import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


if __name__ == '__main__':

    number_of_users = pd.read_csv('data/wifi_users_by_years.csv', delimiter=';', encoding='latin-1')
    wifi_locations = pd.read_csv('data/wifi_points.csv', delimiter=',')
    kiosk_locations = pd.read_csv('data/kiosks.csv', delimiter=',')
    parking_locations = pd.read_csv('data/parking_lots.csv', delimiter=',')
    fuel_stations = pd.read_csv('data/fuel_stations.csv', delimiter=',')

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
    kiosk_locations.rename(columns={'Enlem': 'LATITUDE', 'Boylam': 'LONGITUDE', '_id': 'ID'}, inplace=True)
    print(kiosk_locations.head())

    parking_locations.drop(columns=['PARK_NAME', 'LOCATION_NAME', 'PARK_TYPE_ID', 'PARK_TYPE_DESC', 'COUNTY_NAME'],
                         inplace=True)
    parking_locations.rename(columns={'_id': 'ID'}, inplace=True)
    print(parking_locations.head())


    columns_to_drop = ['BUSINESS_TYPE_DESC', 'FUEL_DISTRIBUTION_COMPANY_ID', 'FUEL_DISTRIBUTION_COMPANY_DESC',
                       'LPG_DISTRIBUTION_COMPANY_ID', 'LPG_DISTRIBUTION_COMPANY_DESC', 'FACILITY_TYPE_ID',
                       'BUSINESS_TYPE_ID', 'COUNTY_UAVT_CODE', 'COUNTY_NAME', 'NEIGHBORHOOD_UAVT_CODE',
                       'NEIGHBORHOOD_NAME', 'FACILITY_TYPE_DESC']
    fuel_stations.drop(columns=columns_to_drop, inplace=True)
    fuel_stations.rename(columns={'LONGTITUDE': 'LONGITUDE'}, inplace=True)

    # Print the first 5 rows of the dataframe
    print(fuel_stations.head())

    # Export dataframes to a csv file
    number_of_users.to_csv('data/export/number_of_users.csv', index=False)
    wifi_locations.to_csv('data/export/wifi_locations.csv', index=False)
    kiosk_locations.to_csv('data/export/kiosk_locations.csv', index=False)
    parking_locations.to_csv('data/export/parking_lots.csv', index=False)
    fuel_stations.to_csv('data/export/fuel_stations.csv', index=False)


import numpy as np

EARTH_RADIUS_KM = 6371

def haversine_km(lat1, lng1, lat2, lng2):
    lat1 = np.radians(lat1)
    lat2 = np.radians(lat2)
    lng1 = np.radians(lng1)
    lng2 = np.radians(lng2)

    dlat = lat2 - lat1
    dlng = lng2 - lng1

    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlng / 2) ** 2
    distance = 2 * EARTH_RADIUS_KM * np.arcsin(np.sqrt(a))
    return distance
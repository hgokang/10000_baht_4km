import googlemaps
from api import *

class ShopFinder:
    def __init__(self, api_key):
        self.api = googlemaps.Client(key=api_key)
    
    def get_user_location(self):
        try:
            user_location = self.api.geolocate()
            return user_location
        except Exception as e:
            print(f"Error getting user location: {str(e)}")
            return None
    
    def find_shop_nearby(self, location, radius=4000, keyword='cafe'):
        try:
            places = self.api.places_nearby(location=location, radius=radius, keyword=keyword)
            return places['results']
        except Exception as e:
            print(f"Error finding shop nearby: {str(e)}")
            return []
    
    def get_distance_info(self, origin, destination):
        try:
            distance_info = self.api.distance_matrix(origins=origin, destinations=destination)
            return distance_info
        except Exception as e:
            print(f"Error getting distance information: {str(e)}")
            return None
    
    def print_shop_info(self, result, user_location):
        for i, shop in enumerate(result):
            name_place = shop['name']
            place_location = shop['vicinity']
            rate = shop.get('rating', 'N/A')
            rating_total = shop.get('user_ratings_total', 'N/A')
            type_ = ', '.join(shop['types'])
            geo_locate_lat = shop['geometry']['location']['lat']
            geo_locate_lng = shop['geometry']['location']['lng']
            destination_locate = f"{geo_locate_lat},{geo_locate_lng}"
            distance_info = self.get_distance_info(user_location, destination_locate)

            print(f"\nชื่อร้าน : {name_place}")
            print(f"location : {place_location}")
            print(f"rating : {rate}")
            print(f"type : {type_}")
            print(f"rating total : {rating_total}")
            print(f"Geo_locate : {geo_locate_lat}, {geo_locate_lng}")
            if distance_info:
                print(f"ระยะทางทั้งหมด : {distance_info['rows'][0]['elements'][0]['distance']['text']}")
                print(f"ระยะเวลาที่ใช้ : {distance_info['rows'][0]['elements'][0]['duration']['text']}")
        
        print(f"จำนวนร้านที่พบ: {i + 1}")

if __name__ == '__main__':
    shop_finder = ShopFinder(api_key)
    
    user_location = shop_finder.get_user_location()
    
    if user_location:
        if user_location['accuracy'] > 4000:
            location = input("กรอกที่อยู่: ")
        else:
            location = f"{user_location['location']['lat']},{user_location['location']['lng']}"
        shops_nearby = shop_finder.find_shop_nearby(location)
        shop_finder.print_shop_info(shops_nearby, location)

import googlemaps


Api = googlemaps.Client(key='Test')
# location = '13.7349125,100.5304545'

find_user_locate = Api.geolocate()                                                          #Api request

find_user_locate_lat = find_user_locate["location"]["lat"]
find_user_locate_lng = find_user_locate["location"]["lng"]

if find_user_locate['accuracy'] > 3000:
    location = input("กรอกที่อยู่")
else:
    location = str(find_user_locate_lat)+','+str(find_user_locate_lng)

find_place = Api.places_nearby(location = location, radius = 4000, keyword = 'cafe')        #Api request
result = find_place['results']

for i in range(len(result)):
    name_place = result[i]['name']
    place_locations = result[i]['vicinity']
    geo_locate_lat = result[i]['geometry']['location']['lat']
    geo_locate_lng = result[i]['geometry']['location']['lng']
    destination_locate = str(geo_locate_lat)+','+str(geo_locate_lng)
    distance = Api.distance_matrix(origins = location,destinations = destination_locate)    #Api request ]Loop
    print(f"\nชื่อร้าน : {name_place}")
    print(f"location : {place_locations}")
    print(f"Geo_locate : {geo_locate_lat,geo_locate_lng}")
    print(f"ระยะทางทั้งหมด : {distance['rows'][0]['elements'][0]['distance']['text']}")
    print(f"ระยะเวลาที่ใช้ : {distance['rows'][0]['elements'][0]['duration']['text']}")

print(f"จำนวนร้านที่พบ{i}")

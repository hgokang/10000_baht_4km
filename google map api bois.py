import googlemaps
########### Steamlit input and output ###########    ###    อย่าลืมทำนะไอน้อง   ###

Api = googlemaps.Client(key='#')
# location = '13.7349125,100.5304545'
file = open('resource_api.txt', 'wb')
find_user_locate = Api.geolocate()                                                          #Api request

find_user_locate_lat = find_user_locate["location"]["lat"]
find_user_locate_lng = find_user_locate["location"]["lng"]

if find_user_locate['accuracy'] > 4000:
    location = input("กรอกที่อยู่")
else:
    location = str(find_user_locate_lat)+','+str(find_user_locate_lng)

place = Api.places_nearby(location = location, radius = 4000, keyword='cafe')        #Api request
result = place['results']

# find_place = Api.find_place(result[1]['name'],input_type='textquery')        #No Need
# print(find_place)
# print(result[1])


for i in range(len(result)):
    name_place = result[i]['name']
    place_locations = result[i]['vicinity']
    rate = result[i]['rating']
    rating_total = result[i]['user_ratings_total']
    type_ = result[i]['types']
    geo_locate_lat = result[i]['geometry']['location']['lat']
    geo_locate_lng = result[i]['geometry']['location']['lng']
    destination_locate = str(geo_locate_lat)+','+str(geo_locate_lng)
    distance = Api.distance_matrix(origins = location,destinations = destination_locate)    #Api request ]Loop
    # file.write(f"{str(geo_locate_lat)} {str(geo_locate_lng)} {distance['rows'][0]['elements'][0]['distance']['text']}\n")
    print(f"\nชื่อร้าน : {name_place}")
    print(f"location : {place_locations}")
    print(f"rating : {rate}")
    print(f"type : {type_}")
    print(f"rating total : {rating_total}")
    print(f"Geo_locate : {geo_locate_lat,geo_locate_lng}")
    print(f"ระยะทางทั้งหมด : {distance['rows'][0]['elements'][0]['distance']['text']}")
    print(f"ระยะเวลาที่ใช้ : {distance['rows'][0]['elements'][0]['duration']['text']}")

print(f"จำนวนร้านที่พบ{i}")


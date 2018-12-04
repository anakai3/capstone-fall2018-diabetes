from googleplaces import GooglePlaces, types, lang

API_KEY = 'AIzaSyDR3mV_8uzxqPDOn3uOYwqfWpjAmBr2XyQ'

google_places = GooglePlaces(API_KEY)

query_result = google_places.nearby_search(
    location='37.36801,-121.92135', 
    radius=10000, types=[types.TYPE_RESTAURANT])

if query_result.has_attributions:
    print (query_result.html_attributions)


for place in query_result.places:
    place.get_details()
    print (place) 

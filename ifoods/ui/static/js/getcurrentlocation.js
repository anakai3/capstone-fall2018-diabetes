var map;
var infowindow;
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    latitude =  position.coords.latitude  
    longitude =  position.coords.longitude; 
    var x = document.getElementById("locdata"); 
    x.value="Lat:"+latitude+",Long:"+longitude;
    console.log(latitude);
    console.log(longitude);
    var pyrmont = new google.maps.LatLng(latitude,longitude);
    //var pyrmont = new google.maps.LatLng(-33.8665433,151.1956316);
    console.log(pyrmont);
    map = new google.maps.Map(document.getElementById('map'), {
      center: pyrmont,
      zoom: 10
    });
    infowindow = new google.maps.InfoWindow();
    var service = new google.maps.places.PlacesService(map);
    service.nearbySearch({
          location: pyrmont,
          radius: 5000,
          type: ['restaurant']
        }, callback);
}

function callback(results, status) {
          console.log(status);
        if (status === google.maps.places.PlacesServiceStatus.OK) {
          console.log("hello");
        
          if (results.length == 0) document.getElementById("curlocres").innerHTML = "<option></option>";
          else {
            var catOptions = "";
            for (var i = 0; i < results.length; i++) {
                createMarker(results[i]);
                console.log(results[i].name);
                catOptions += "<option>" + results[i].name + "</option>";
             }
          }
          document.getElementById("curlocres").innerHTML = catOptions;
        }
}

function createMarker(place) {
        var placeLoc = place.geometry.location;
        var marker = new google.maps.Marker({
          map: map,
          position: place.geometry.location
        });

        google.maps.event.addListener(marker, 'click', function() {
          infowindow.setContent(place.name);
          infowindow.open(map, this);
        });
}

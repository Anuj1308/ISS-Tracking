import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("There are currently" + str(result["number"]) + " astronauts on the ISS: \n\n") 
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")

g = geocoder.ip('me')
file.write("\n Your current latitude/ longitude is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

#setup the world map in turtle module

screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

#load the world map

screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
    #load the current status of the  ISS in rea-time
    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    #Ectract the ISS location
    location = result("iss_position")
    lat = location['latitude']
    lon = location['longitude']

    #Output lolngitude and latitude to the terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    #Update the ISS location on the map
    iss.goto(lon, lat)
    #Referesh each 5 seconds
    time.sleep(10)
    #screen.ontimer(update_iss_position, 5000)  # Schedule the next update in 5 seconds

# Start updating the ISS position
#update_iss_position()

# Start the turtle main loop
#turtle.mainloop()

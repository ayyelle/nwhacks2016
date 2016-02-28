from flask import Flask, render_template, request,json,jsonify, redirect
import urllib
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html");

@app.route('/getact', methods = ['POST'])
def getact():
    acttype = request.form['acttype']
    lati = request.form['lat']
    longi = request.form['lon']
    distance = int(request.form['distance'])
    distance = distance*1000
    dist = str(distance)
    print(acttype)
    print(lati)
    print(longi)
    print(distance)
    if acttype=="food":
        url = "https://developers.zomato.com/api/v2.1/search?lat="+lati+"&lon="+longi+"&radius="+dist+"&apikey=40b2fe93e6a1e1e123e6f67b846a5696"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        amount = int(data["results_shown"]);
        listOfLatLon = [];
        for i in range (0,amount):
         lat = data["restaurants"][i]["restaurant"]["location"]["latitude"]
         lon = data["restaurants"][i]["restaurant"]["location"]["longitude"]
         coordinates = [float(lat),float(lon)]
         listOfLatLon.append(coordinates)

        name = "Map"
        latitude = data["restaurants"][2]["restaurant"]["location"]["latitude"]
        longitude = data["restaurants"][2]["restaurant"]["location"]["longitude"]
        user = {'nickname': "Anna"}
        return render_template('index2.html',title=name,user=user,latitude=lati,longitude=longi,listOf=listOfLatLon)

    elif acttype=="bus":
        url = "http://api.translink.ca/rttiapi/v1/stops?apikey=tnQyev7bLMYr6y43Cs2e&lat="+lati+"&long="+longi+"&radius="+dist
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        amount = int(data["results_shown"]);
        listOfLatLon = [];
        for i in range (0,amount):
         lat = data["restaurants"][i]["restaurant"]["location"]["latitude"]
         lon = data["restaurants"][i]["restaurant"]["location"]["longitude"]
         coordinates = [float(lat),float(lon)]
         listOfLatLon.append(coordinates)

        name = "Map"
        latitude = data["restaurants"][2]["restaurant"]["location"]["latitude"]
        longitude = data["restaurants"][2]["restaurant"]["location"]["longitude"]
        user = {'nickname': "Anna"}
        return render_template('index2.html',title=name,user=user,latitude=lati,longitude=longi,listOf=listOfLatLon)

   # return redirect('/')

if __name__ == '__main__':
    app.run()
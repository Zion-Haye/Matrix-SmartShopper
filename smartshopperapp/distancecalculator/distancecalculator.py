import json
import requests



def get_google_response(branch_location , user_location):

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Arima,Trinidad&destinations= Trincity Mall, Piarco&units=imperial&key=AIzaSyBdKVFYnmEYRYPAeH2zspx0JK3CPkFdOJc"

    payload={}
    headers = {}

    url1 = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="
    url2 = user_location
    url3 = "&destinations= "
    url4 = branch_location
    url5 = "&units=imperial&key=AIzaSyBdKVFYnmEYRYPAeH2zspx0JK3CPkFdOJc"

    fullurl = url1 + url2 + url3 + url4 + url5

    response = requests.request("GET", fullurl, headers=headers, data=payload)

    print(response.text)

    responsejson = response.json()

    responsejsonelements = responsejson["rows"][0]
    status = responsejsonelements["elements"][0]["status"]
    print("Status")
    print(status)
 
    if status == "OK":
        print("Distance")
    
        
        distance = responsejsonelements["elements"][0]["distance"]["text"]

        print(distance)

        print("Duration")
        duration = responsejsonelements["elements"][0]["duration"]["text"]
        print(duration)

        googleAPIresponse = {}
        googleAPIresponse["duration"] = duration
        googleAPIresponse["distance"] = distance

    else:
        googleAPIresponse = {}
        googleAPIresponse["duration"] = "Not Found"
        googleAPIresponse["distance"] = "Not Found"


    return googleAPIresponse



import requests
import json
from pickle import dump , load
import sys
from routehome.settings import MapQuest_API


class Send_Data:
    """ class that creates the data to send to mapquestapi
    and converts it with Json"""

    def __init__(self, start, end, points):
        self.start = start
        self.end = end
        self.points = points
        self.Data()
        self.data = json.dumps(self.data)
        self.Get_Directions()
        # print(self.data)

    def Data(self):
        self.data = {}
        self.data['locations'] = [
            {
                "latLng": {
                    "lat": self.start[0],
                    "lng": self.start[1]
                    }
                },
            {
                "latLng": {
                    "lat": self.end[0],
                    "lng": self.end[1]
                    }
                }
            ]
        self.Options()
        self.data['options'] = self.options
        self.data['routeControlPointCollection'] = self.points
        print(self.data)

    def Options(self):
        self.options = {}
        self.options['avoids'] = []
        self.options['avoidTimedConditions'] = False
        self.options['doReverseGeocode'] = True
        self.options['shapeFormat'] = 'raw'
        self.options['generalize'] = 0
        self.options['routeType'] = 'pedestrian'
        self.options['timeType'] = 1
        self.options['locale'] = 'en_US'
        self.options['unit'] = 'm'
        self.options['enhancedNarratives'] = False
        self.options['drivingStyle'] = 2
        self.options['highwayEfficiency'] = 21


    def Get_Directions(self):
        url='http://www.mapquestapi.com/directions/v2/route?key=%s' % (MapQuest_API)
        self.response = requests.post(url, data=self.data)
        # Handle 500 Erros with pytho's request api

        self.response = self.response.json()
        print(self.response)
        return self.response

    def Store_Directions(self):
        Directions = open(Directions, 'wb')
        dump(self.directions, Directions) # move this to a template, template displays stuff to user
        Directions.close()


if __name__ == '__main__':
    mydata = Send_Data("Clarendon Blvd, Arlington, VA","2400 S Glebe Rd, Arlington, VA",)
    #response = requests.post(url, data=mydata.data)
    #print (response.json())
    #response = response.json()
    print(mydata.response['route']['legs'])

    print(mydata.data)

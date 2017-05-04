import requests
import json
from pickle import dump , load
import sys
from routehome.settings import MapQuest_API


class Send_Data:
    """ Class that creates the data to send to mapquestapi
    and converts it with Json"""

    def __init__(self, start, end, points):
        """
        Arguuments:
        start: tuple of latitude and longitude
        end: tuple of latitude and longitude
        points: list of latitude and longitude tuples
        """
        self.start = start
        self.end = end
        self.points = points
        self.Data()
        self.data = json.dumps(self.data) #Converts Data into a json Object
        self.Get_Directions()

    def Data(self):
        """
        Creates and populates dataset with data from website
        """
        self.data = {}
        self.data['locations'] = [ #defining the lat/long dictionaries for start and end locations
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
        self.Options() #Calls the Options method
        self.data['options'] = self.options
        self.data['routeControlPointCollection'] = self.points # creates the dictionary filled with the routeControlPointCollection

    def Options(self):
        """
        Sets options for Mapquest API
        """
        self.options = {}
        self.options['tryAvoidLinkIds'] = []
        if len(self.points) < 100:
            for crimept in self.points:
                try:
                    IDurl = 'http://www.mapquestapi.com/directions/v2/findlinkid?key=%s&lat=%f&lng=%f' % (
                        MapQuest_API, crimept['lat'], crimept['lng'])
                    idData = requests.get(IDurl)
                    linkId = str(idData.json()['linkId'])
                    self.options['tryAvoidLinkIds'].append(linkId)
                except Exception as e:
                    continue
        self.options['avoidTimedConditions'] = False
        self.options['doReverseGeocode'] = True
        self.options['shapeFormat'] = 'raw'
        self.options['generalize'] = 0
        self.options['routeType'] = 'pedestrian' #walking directions
        self.options['timeType'] = 1
        self.options['locale'] = 'en_US'
        self.options['unit'] = 'm'
        self.options['enhancedNarratives'] = False
        self.options['drivingStyle'] = 2
        self.options['highwayEfficiency'] = 21
        self.options['highwayEfficiency'] = 21 #miles per galon (not relevant)



    def Get_Directions(self):
        """
        Gets directions from Mapquest
        """
        url='http://www.mapquestapi.com/directions/v2/route?key=%s' % (MapQuest_API)
        self.response = requests.post(url, data=self.data)
        # Handle 500 Erros with pytho's request api

        self.response = self.response.json()
        return self.response

    def Store_Directions(self):
        """
        Pickles directions for use by the website
        """
        Directions = open(Directions, 'wb')
        dump(self.directions, Directions) # move this to a template, template displays stuff to user
        Directions.close()


if __name__ == '__main__':
    mydata = Send_Data("Clarendon Blvd, Arlington, VA", "2400 S Glebe Rd, Arlington, VA")
    print(mydata.response['route']['legs'])

    print(mydata.data)

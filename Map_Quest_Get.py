import requests
import json
from pickle import dump , load
import sys
from routehome.settings import MapQuest_API


class Send_Data:
    """ class that creates the data to send to mapquestapi
    and converts it with Json"""

    def __init__(self, start, end, points):
        # Init method that calles each of the other method as well as adding the
        # Start and end locations in the data set
        self.start = start
        self.end = end
        self.points = points
        self.Data()
        self.data = json.dumps(self.data) #Converts Data into a json Object
        self.Get_Directions()
        # print(self.data)

    def Data(self):
        #Creates the Data set and begins to fill it
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
        # print(self.points)

    def Options(self):
        #names the other(constant) options for the directions request
        self.options = {}
        self.options['tryAvoidLinkIds'] = []
        if len(self.points) < 100:
            for crimept in self.points:
                print(crimept)
                try:
                    IDurl = 'http://www.mapquestapi.com/directions/v2/findlinkid?key=%s&lat=%f&lng=%f' % (
                        MapQuest_API, crimept['lat'], crimept['lng'])
                    print('id url got')
                    idData = requests.get(IDurl)
                    print('got id data')
                    print(idData.content)
                    linkId = str(idData.json()['linkId'])
                    print('got linkid')
                    self.options['tryAvoidLinkIds'].append(linkId)
                    print('got it to append')
                except Exception as e:
                    print(e)
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
        self.options['highwayEfficiency'] = 21 #miles per galon (not relevant)
    # def Get_AvoidLinkIDs(self):
    #     for crimept in self.points:
    #         IDurl = 'http://www.mapquestapi.com/directions/v2/findlinkid?key=%s&lat=%f&lng=%f' % (
    #             MapQuest_API, crimept['lat'], crimept['lng'])
    #         json = requests.get(IDurl).json()
    #         self.options['tryAvoidLinkIds'].append = json['linkId']

    def Get_Directions(self):
        # print(self.Data)
        url='http://www.mapquestapi.com/directions/v2/route?key=%s' % (MapQuest_API)
        self.response = requests.post(url, data=self.data)
        # Handle 500 Erros with pytho's request api

        self.response = self.response.json()
        # print(self.response)
        return self.response

    def Store_Directions(self):
        #pickels the response from Mapquest into a file called Directions
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

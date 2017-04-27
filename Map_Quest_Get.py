import requests
import json
from pickle import dump , load
import sys




class Send_Data:
    """ class that creates the data to send to mapquestapi
    and converts it with Json"""

    def __init__(self, start, end, points):
        self.start = start
        self.end = end
        self.Data()
        self.data['routeControlPointCollection'] = points
        self.data = json.dumps(self.data)
        self.Get_Directions()



    def Data(self):
        self.data = {}
        self.data['locations'] = [self.start, self.end]
        self.Options()
        self.data['options']= self.options

    def Options(self):
        self.options = {}
        self.options['avoids'] = []
        self.options['avoidTimedConditions'] = False
        self.options['doReverseGeocode'] = True
        self.options['shapeFormat'] = 'raw'
        self.options['generalize'] = 0
        self.options['routeType'] = 'fastest'
        self.options['timeType'] = 1
        self.options['locale'] = 'en_US'
        self.options['unit'] = 'm'
        self.options['enhancedNarratives'] = False
        self.options['drivingStyle'] = 2
        self.options['highwayEfficiency'] = 21


    def Get_Directions(self):
        url='http://www.mapquestapi.com/directions/v2/route?key=myLzT3Tf3PjQVNlYNuPhVCU7jxBP0wVG'
        self.response = requests.post(url, data=self.data)
        # Handle 500 Erros with pytho's request api

        self.response = self.response.json()

        return self.response



    def Store_Directions(self):
        Directions = open(Directions,'wb')
        dump(self.directions,Directions) # move this to a template, template displays stuff to user
        Directions.close()

if __name__ == '__main__':
    mydata = Send_Data("Clarendon Blvd, Arlington, VA","2400 S Glebe Rd, Arlington, VA",)
    #response = requests.post(url, data=mydata.data)
    #print (response.json())
    #response = response.json()
    print (mydata.response['route']['legs'])

    print (mydata.data)

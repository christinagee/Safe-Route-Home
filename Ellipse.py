import math
class Ellipse(object):

    def __init__(self, x1, y1, x2, y2):
        """
        Arguments: int x1, int y1, int x2, int y2
        Attributes:
        tuple focus1
        tuple focus2
        tuple center
        int eccentricity
        int angle (radians)
        int semiminor (semi-minor axis)
        int edgeDist(distance from edge to foci)
        """
        self.focus1 = (x1, y1)
        self.focus2 = (x2, y2)
        self.center = ((x1+x2)/2, (y1 + y2)/2)
        self.eccentricity = 0.5
        self.angle = math.atan((self.focus2[1] - self.focus1[1])/(self.focus2[0] - self.focus1[0]))
        self.semiminor = (self.calcDistBetweenFocus()/2)/self.eccentricity
        self.edgeDist = 2*self.calcDistToVertex()

    def calcDistBetweenFocus(self):
        """
        Calculates the distance between the focuses of the Ellipse.
        """
        return math.sqrt((self.focus2[0] - self.focus1[0])**2 + (self.focus2[1] - self.focus1[1])**2)

    def calcDistToVertex(self):
        """
        Calculates Distance between vertex on semi-minor axis of ellipse and focus.
        Uses pythagorean theorem
        """
        return math.sqrt(self.semiminor**2 + (self.calcDistBetweenFocus()/2)**2)

    def distToFocus1(self, x, y):
        """
        Calculates distance to focus 1 of the ellipse from point x, y
        Arguments: int x, int y
        """
        return math.sqrt((x-self.focus1[0])**2 + (y-self.focus1[1])**2)

    def distToFocus2(self, x, y):
        """
        Calculates distance to focus 2 of the ellipse from point x, y
        Arguments: int x, int y
        """
        return math.sqrt((x-self.focus2[0])**2 + (y-self.focus2[1])**2)

    def isWithinEllipse(self, x, y):
        """
        Checks whether a point is within ellipse.
        Is the total distance to the foci less than the distance
        from a vertex to the foci?
        """
        dist = self.distToFocus1(x, y) + self.distToFocus2(x, y)

        if dist <= self.edgeDist:
            return True
        else:
            return False

if __name__ == "__main__":
    ellipse = Ellipse(1, 2, 4, 5)
    print(ellipse.isWithinEllipse(3, 4))

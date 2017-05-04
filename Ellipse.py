import math
import unittest
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
        self.eccentricity = 2
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
        from a vertex to the foci
        """
        dist = self.distToFocus1(x, y) + self.distToFocus2(x, y)

        if dist <= self.edgeDist:
            return True
        else:
            return False


class TestEllipse(unittest.TestCase):

    def setUp(self):
        """
        Runs before unitTests.
        Function sets up test Ellipse with foci at
        (1, 0) and (2, 0) and eccentricity of 5
        """
        self.ell = Ellipse(1, 0, 2, 0)

    def test_dist_btw_foci(self):
        """
        Function tests calcDistBetweenFocus Function
        """

        self.assertEqual(self.ell.calcDistBetweenFocus(), 1)

    def test_dist_to_vertex(self):
        """
        Function tests calcDistToVertex Function
        """
        self.assertEqual(self.ell.calcDistToVertex(), math.sqrt(0.25+0.0625))

    def test_dist_to_focus1(self):
        """
        Function tests distToFocus1
        """

        self.assertEqual(self.ell.distToFocus1(0, 0), 1)

    def test_dist_to_focus2(self):
        """
        Function tests distToFocus2
        """
        self.assertEqual(self.ell.distToFocus2(0, 0), 2)


    def test_is_within_ellipse(self):
        """
        Function tests isWithinEllipse
        with point halfway btw focuses
        """
        self.assertTrue(self.ell.isWithinEllipse(1.5, 0))


if __name__ == "__main__":
    unittest.main()

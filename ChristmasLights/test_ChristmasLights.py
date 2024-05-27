from ChristmasLights import Lights
import unittest

class TestChristmasLights(unittest.TestCase):
    
    def test_light_first_line(self):
        lights = Lights()
        lights.turnOn("0,0","1,0")
        self.assertEqual(lights.getOn(),1001)

    def test_light_second_line(self):
        lights = Lights()
        lights.turnOn("1,0","1,999")
        self.assertEqual(lights.getOn(),1000)

    def test_light_first_second_line(self):
        lights = Lights()
        lights.turnOn("0,0","1,999")
        self.assertEqual(lights.getOn(),2000)
        
    def test_light_whole(self):
        lights = Lights()
        lights.turnOn("0,0","999,999")
        self.assertEqual(lights.getOn(),1000000)
    

if __name__ == '__main__':
    unittest.main()
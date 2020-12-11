<<<<<<< HEAD
class Town:

    def __init__(self, name):
        self.name = name

    def set_latitude(self, latitude: str):
        self.latitute = latitude

    def set_longitude(self, longitude: str):
        self.longitute = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitute} | Longitude: {self.longitute}"


town = Town("Sofia")
town.set_longitude("42° 41\' 51.04\" N")
town.set_latitude("23° 19\' 26.94\" E")
print(town)
=======
class Town:

    def __init__(self, name):
        self.name = name

    def set_latitude(self, latitude: str):
        self.latitute = latitude

    def set_longitude(self, longitude: str):
        self.longitute = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitute} | Longitude: {self.longitute}"


town = Town("Sofia")
town.set_longitude("42° 41\' 51.04\" N")
town.set_latitude("23° 19\' 26.94\" E")
print(town)
>>>>>>> 208b47ea4d0bcafc85cf570be2bfb1f6ac828c17

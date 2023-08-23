import json 

class Point:
    def __init__(self, name: str, x: float, y: float) -> None:
        self.name = name
        self.x = x
        self.y = y

    def getJSONFormat(self):
        d = {
            "name": self.name,
            "x": self.x,
            "y": self.y
        }

        return json.dumps(d)

p = Point("SignalQ", 1.2, 2.2)
print(p.getJSONFormat())
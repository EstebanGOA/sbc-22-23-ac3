class Connection:

    def __init__(self, to, distance, duration):
        self.to = to
        self.distance = distance
        self.duration = duration

    def getTo(self):
        return self.to

    def getDistance(self):
        return int(self.distance)

    def getDuration(self):
        return int(self.duration)

class Apartment:
    def __init__(self, type, price, square_meter, street, room, link, created, fetched):
        self.type = type
        self.price = price
        self.square_meter = square_meter
        self.street = street
        self.room = room
        self.link = link
        self.created = created
        self.fetched = fetched

    def __str__(self):
        return 'type ' + self.type + ", price " + str(self.price) + ", square_meter " + str(self.square_meter) + ", street " + self.street + ", room " + str(self.room) + ", link " + self.link + ", created " + self.created + ", fetched " + self.fetched

    def is_cheap(self):
        return self.price < 4000

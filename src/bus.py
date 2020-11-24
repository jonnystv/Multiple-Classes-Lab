class Bus:

    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []


    def drive(self):
        return "Brum brum"

    
    def passenger_count(self):
        return len(self.passengers)#Probably shouldn't have used 'person' in this one as it's the name of a class


    def pick_up(self, person):
        self.passengers.append(person)#Probably shouldn't have used 'person' in this one as it's the name of a class


    def drop_off(self, person):
        self.passengers.remove(person)#Probably shouldn't have used 'person' in this one as it's the name of a class


    def empty(self):
        self.passengers.clear()
        #OR self.passengers = []

    def pick_up_from_stop(self, bus_stop):
        bus_stop.queue.clear()

    def pick_up_from_stop(self, bus_stop_to_pick_up_from) :
        for passenger in bus_stop_to_pick_up_from.queue:
            self.pick_up(passenger) 
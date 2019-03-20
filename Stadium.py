class Stadium:
    _number_of_created_stadiums = 0

    def __init__(self, name="unknown", number_of_spectators="unknown",
                 power_of_lightning="unknown", maximal_number_of_spectators="unknown",
                 number_of_parking_spots="unknown", number_of_enters="unknown"):
        Stadium._number_of_created_stadiums += 1
        self.name = name
        self.number_of_spectators = number_of_spectators
        self.maximal_number_of_spectators = maximal_number_of_spectators
        self.power_of_lightning = power_of_lightning
        self.number_of_parking_spots = number_of_parking_spots
        self.number_of_enters = number_of_enters

    def __del__(self):
        Stadium._number_of_created_stadiums -= 1
        print (self.name + " stadium was destructed")

    def __str__(self):
        return "name: " + self.name \
               + ", number of spectators: " + str(self.number_of_spectators) \
               + ", maximal number of spectators: " + str(self.maximal_number_of_spectators) \
               + ", power of lightning: " + str(self.power_of_lightning) \
               + ", number of parking spots: " + str(self.number_of_parking_spots) \
               + ", number of enters: " + str(self.number_of_enters)

    @staticmethod
    def get_static_number_of_created_stadiums():
        return Stadium._number_of_created_stadiums


print 'Number of created stadiums:', Stadium.get_static_number_of_created_stadiums()
unknown = Stadium()
print unknown
print "\n"
print 'Number of created stadiums:', Stadium.get_static_number_of_created_stadiums()
silskiy = Stadium(number_of_spectators=20, number_of_enters=1, number_of_parking_spots=0)
print silskiy
print "\n"
print 'Number of created stadiums:', Stadium.get_static_number_of_created_stadiums()
wembley = Stadium(name='Wembley', number_of_parking_spots=400, number_of_enters=20, number_of_spectators=40000)
print wembley
print "\n"
print 'Number of created stadiums:', Stadium.get_static_number_of_created_stadiums()
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    #Can use this function to show what is inside, not the memory location
    # def __str__(self):
    #     return self.price

    def displayInfo(self):
        print 'Price is: $' + str(self.price)
        print 'Max Speed: ' + str(self.max_speed) + 'mph'
        print 'Total miles:' + str(self.miles) + 'miles'
        
    def drive(self):
        print "Riding "
        self.miles += 10
        
    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        

bike1 = Bike(12, 50)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(15, 25)
bike2.drive()
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(8, 35)
bike3.drive()
bike3.drive()
bike3.drive()
bike3.reverse()
bike3.displayInfo()


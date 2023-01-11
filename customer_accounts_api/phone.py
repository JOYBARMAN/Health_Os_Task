from .models import Customer
import random
# create a class for generate a unique number 

class UniqueNumber():

# now create a function generate a banngladeshi phone number
    def randomNumGenerator(self):
        randomNum = "+880" 
        # Bangladesh all operator code num
        operator = ["17","19","16","15","18","13"]
        randomOperator = random.choice(operator)
        # add random operator value in random num 
        randomNum += randomOperator
        # now pick last 8 digit 
        for i in range(8):
            randomDigit = random.randint(0,9)
            randomNum += str(randomDigit)
        return randomNum

# now make number is unique 
    def uniqueNumber(self):
        try:
            number = self.randomNumGenerator()
            if Customer.objects.filter(phone=number).exists():
                anotherNum = self.randomNumGenerator()
                number = anotherNum
            return number
        except Exception as e:
            print(e)

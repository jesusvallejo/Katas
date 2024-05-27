
class Lights(object):
    
    def __init__(self):
        self.light = []

    def turnOn(self,begin,end):
        self.light = self.light + (self.decode(end)+1 - self.decode(begin))
        
    def turnOff(self,begin, end):
        if (self.light >0):
            self.light = self.light - (self.decode(end)+1 - self.decode(begin))
                   
    def getOn(self):
        return self.light

    def decode(self,position):
        a,b = position.split(',')
        x=int(b)
        y=int(a)
        n=1000
        if(x == 0 and y == 0):
            return 0
        elif(x==0):
            return (y*n)
        elif(y==0):
            return x
        else:
            return x + (y*n)
class taxi:
    def __init__(self):
        self.distance=int(input("enter the distance you have to travel:"))
        self.timeofday=input("enter the current time:").split()
        self.prev_rides=int(input("enhter the nuumber of previous rides travelled:"))
    
    def cal_distance(self):
        if(self.distance>0 and self.distance<=5):
            self.charge=50
        elif(self.distance<=15):
            self.charge= 8*(self.distance-5) +50
        else:
            self.charge= (10*(self.distance-15)) + 80
    
    def cal_surcharge(self):
        self.time=int(self.timeofday[0])
        self.surcharge=0
        if(self.time>=5 and self.time<=8 and "pm" in self.timeofday):
            self.surcharge=(self.charge*25)//100
    
    def cal_discount(self):
        self.discount=0
        if(self.prev_rides>20):
            self.discount=(self.charge*15)//100
        
    def total_fare(self):
        self.cal_distance()
        self.cal_surcharge()
        self.cal_discount()
        self.fare=(self.charge+self.surcharge)-self.discount
        if(self.distance>0 and self.time>=1 and self.time<=12) :
            print(self.fare)
        else:
            print("-1")
obj=taxi()
obj.total_fare()





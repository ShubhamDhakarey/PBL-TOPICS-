class ticket:
    week=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    def __init__(self):
        self.days=str(input("enter the day :"))
        self.quantity=int(input("enter number of tickets :"))
        self.age=int(input("enter your age :"))
    def cal_age(self):
        if(self.age<=12):
            self.price=100
        elif(self.age<=59):
            self.price=150
        else:
            self.price=120
    def cal_discount(self):
        self.discount1=0
        self.discount2=0
        if(self.quantity>5):
            self.discount1=(self.price*10)//100
        if(self.days=="saturday" or self.days=="sunday"):
            self.discount2=(self.price*20)//100
        if(self.quantity>5 or (self.days=="saturday" or self.days=="sunday")):
            self.final_discount=self.discount1+self.discount2
        else:
            self.final_discount=0
    def bill(self):
        self.cal_age()
        self.cal_discount()
        if(self.quantity>1 and self.age>0 and (self.days in self.week)):
            self.amount=self.price-self.final_discount
            print("bill :",self.amount)
        else:
            print("-1")
theatre=ticket()
theatre.bill()
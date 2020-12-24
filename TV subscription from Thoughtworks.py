class Customer:
    count=0
    def __init__(self):
        self.name="John Doe"
        self.Account_Balence=1000
        self.current_subscription=["PQR","Base"]
    
    def display(self):    
        print("Name :",self.name)
        print("Account Balence :",self.Account_Balence)
        print("current subscription :",self.current_subscription)
        print() 


class Television(Customer):
    
    def ABC_channel(self,channel):
        pack={"Base":120,"SD":130,"HD":150,"4k":200}
        print("please choose subscription type: (Base,SD,HD,4K)")
        plan=input().strip()
        if(plan!=tv.current_subscription[1]):
            tv.reduction(pack,plan,channel)
        else:
            print("That pack is already choosen")
        
        
    def PQR_channel(self,channel):
        pack={"Base":120,"SD":130}
        print("please choose subscription type: (Base,SD)")
        plan=input().strip() 
        if(plan!=tv.current_subscription[1]):
            tv.reduction(pack,plan,channel)
        else:
            print("That pack is already choosen")

        
        
        
    def reduction(self,pack,plan,channel):
        if(plan in pack.keys()):
            tv.Account_Balence=tv.Account_Balence-pack[plan]
            print("channel {} Subscription was successful".format(plan))
            tv.current_subscription[0]=channel
            tv.current_subscription[1]=plan
            print()
            
        else:
            print("There is no such plan")
     

   
    
    def channel(self):
        print("Enter Channel Name")
        channel=input().strip()
        if(channel in ["ABC","PQR"]):
            if(channel=="ABC"):
                tv.ABC_channel(channel)
            elif(channel=="PQR"):
                tv.PQR_channel(channel)
        else:
            print("There is no kind of channel")

    def subscribe(self):
        tv.channel()
         
    def upgrade(self):
        channel()
        
    def get_deatils(self):
        print("Do you want to subscribe or update?")
        user=input().strip()
        if(user=="subscribe"):
            tv.subscribe()
        elif(user=="upgrade"):
            upgrade()

    ''
tv=Television()
tv.display()
tv.get_deatils()
while(1):
    print("continue?<y/n>")
    a=input().strip()
    if(a=="y"):
        tv.display()
        tv.get_deatils()
    else:
        break


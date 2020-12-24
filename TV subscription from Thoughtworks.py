                                                                    Channel Subscription
As a cable TV operator, I want to provide my customers the ability to subscribe to a channel of their choice and upgrade to different packs based on their preference. 
A customer has a certain balance in his/her account and wishes to subscribe to a channel. The channel should get added to the list of subscribed channels for the customer.
A customer might also wish to upgrade an existing channel he/she has already subscribed to. This should be allowed if an upgrade is possible for the channel. All of the
above should be allowed as long as the customer has the required minimum balance needed for subscription/upgrade. After the subscription/upgrade the difference amount 
should be reflected immediately in the customer’s account.

Hardcoded Data:
List of channels, with the possible upgrades. Eg:
    
ABC Channel:
Base: 120 INR
SD: 130 INR
HD: 150 INR
4k: 200 INR
Allowed Locations: USA, Canada
    
PQR Channel:
Base: 120 INR
SD: 130 INR
Allowed Locations: All
    
Customer Details:
Name: John Doe
Account Balance: 1000 INR
Currently Subscribed Channels: PQR (Base)
    
Input:
Do you want to subscribe or upgrade?
Subscribe
Enter Channel Name
ABC
Please choose subscription type: (Base, SD, HD, 4k)
4k

O/p:
Channel ABC (4k) subscribed successfully.
Available account balance: 800 INR
Continue? <y/n>
Y

Input:
Do you want to subscribe or upgrade?
Upgrade
Enter Channel Name
PQR
Please choose subscription type: (Base, SD)
SD

O/p:
Channel PQR (SD) subscribed successfully.
Available account balance: 790 INR


PROGRAM:
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


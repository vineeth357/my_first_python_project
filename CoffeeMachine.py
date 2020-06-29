#print("The coffee machine has:\n400 of water\n540 of milk\n120 of coffee beans\n9 of disposable cups\n550 of money")

#$550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
class CoffeeMachine:
    
    cash = 550
    water = 400
    milk = 540
    beans = 120
    cups = 9
    core = ['cash','water','milk','beans','cups']
    
    def input(action):
        if (action=='buy'):
            CoffeeMachine.buy()
        elif (action=='fill'):
            CoffeeMachine.fill()
        elif (action=='take'):
            CoffeeMachine.take()
        elif(action=='remaining'):
            CoffeeMachine.remaining()

    def remaining():
        print('The coffee machine has:\n',CoffeeMachine.water,' of water\n',CoffeeMachine.milk,' of milk\n',CoffeeMachine.beans,
        ' of coffee beans\n',CoffeeMachine.cups,' of disposable cups\n',CoffeeMachine.cash,' of money')

    def buy():
        
        
        item = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        
        if(item=='back'):
            CoffeeMachine.buy()
        if(item=='remaining'):
            CoffeeMachine.remaining()
        try:
            item = int(item)
        except:
            item = item
        
        #For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
        #For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
        #And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.
        if item==1:
            if(CoffeeMachine.water<250):
                print('Sorry, not enough water!')
            if(CoffeeMachine.beans<16):
                print('Sorry, not enough beans!')
            if(CoffeeMachine.cups==0):
                print('Sorry, not enough cups!')
            elif(CoffeeMachine.water>250 and CoffeeMachine.beans>16 and CoffeeMachine.cups>0):
                print('I have enough resources, making you a coffee!')
                CoffeeMachine.water = CoffeeMachine.water - 250
                CoffeeMachine.beans = CoffeeMachine.beans - 16
                CoffeeMachine.cash = CoffeeMachine.cash + 4
                CoffeeMachine.cups -= 1
        elif item==2:
            if(CoffeeMachine.water<350):
                print('Sorry, not enough water!')
            if(CoffeeMachine.milk<75):
                print('Sorry, not enough milk!')
            if(CoffeeMachine.beans<20):
                print('Sorry, not enough beans!')
            if(CoffeeMachine.cups==0):
                print('Sorry, not enough cups!')
            elif(CoffeeMachine.water>350 and CoffeeMachine.milk>75 and CoffeeMachine.beans>20 and CoffeeMachine.cups>0):
                print('I have enough resources, making you a coffee!')
                CoffeeMachine.water = CoffeeMachine.water - 350
                CoffeeMachine.milk = CoffeeMachine.milk - 75
                CoffeeMachine.beans = CoffeeMachine.beans - 20
                CoffeeMachine.cash = CoffeeMachine.cash + 7
                CoffeeMachine.cups -= 1
        elif item==3:
            if(CoffeeMachine.water<200):
                print('Sorry, not enough water!')
            if(CoffeeMachine.milk<100):
                print('Sorry, not enough milk!')
            if(CoffeeMachine.beans<12):
                print('Sorry, not enough beans!')
            if(CoffeeMachine.cups==0):
                print('Sorry, not enough cups!')
            elif(CoffeeMachine.water>200 and CoffeeMachine.milk>100 and CoffeeMachine.beans>12 and CoffeeMachine.cups>0):
                print('I have enough resources, making you a coffee!')
                CoffeeMachine.water = CoffeeMachine.water - 200
                CoffeeMachine.milk = CoffeeMachine.milk - 100
                CoffeeMachine.beans = CoffeeMachine.beans - 12
                CoffeeMachine.cash = CoffeeMachine.cash + 6
                CoffeeMachine.cups -= 1
        elif(item!=1 and item!=2 and item!=3 and item!='back'):
            print("sorry!! sir, we don't serve here")
        

    def fill():
        
        add_water = int(input('Write how many ml of water do you want to add:'))
        add_milk = int(input('Write how many ml of milk do you want to add:'))
        add_beans = int(input('Write how many grams of coffee beans do you want to add:'))
        add_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
        CoffeeMachine.milk = CoffeeMachine.milk + add_milk
        CoffeeMachine.water = CoffeeMachine.water + add_water
        CoffeeMachine.beans = CoffeeMachine.beans + add_beans
        CoffeeMachine.cups = CoffeeMachine.cups + add_cups
        
        
    def take():
        print('I gave you ',CoffeeMachine.cash)
        CoffeeMachine.cash = 0

    

while(1):
    action = input('Write action (buy, fill, take,remaining,exit):' )

    if(action=='exit'):
        break
    elif(action in ['buy', 'fill', 'take','remaining']):
        CoffeeMachine.input(action)
    else :
        print('Error!!')
    
    

    

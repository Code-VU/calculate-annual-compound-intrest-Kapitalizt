def calculateCompoundInterest():
    def calc(principal, time, rate):
        amount = principal*(1+(rate/100))**time
        compound_interest = amount - principal
        print("Compound Interest: "+str(round(compound_interest,2)))

    client_one_principal = float(input("Principle (amount): "))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               ")) 
    calc(client_one_principal,client_one_time,client_one_rate)       
    print('---')
    client_two_principal = float(input("Principle (amount): "))
    client_two_time =      float(input("Time:               "))
    client_two_rate =      float(input("Rate:               ")) 
    calc(client_two_principal,client_two_time,client_two_rate)       
    print('---')
    client_three_principal = float(input("Principle (amount): "))
    client_three_time =      float(input("Time:               "))
    client_three_rate =      float(input("Rate:               ")) 
    calc(client_three_principal,client_three_time,client_three_rate)       
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

# calculateCompoundInterest()

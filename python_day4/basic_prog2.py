## The below program demostrate the use of standard Application Program ##
## We are using - while, try-except, user input, type casting functions ##

name = input("What is your name?")

print(f"Hello {name}")

print('Area calculator :')


while True:

    press_check = input('Enter Q to quit :')
    if press_check != 'Q':
        len = input('\n Enter length - ')
        bre = input('\n Enter width  - ')
        
        try:
            area = int(len) * int(bre)
            print(f"Area is {area}")
        except:
            pass
            print("\nEnter new value, entered value are incorrect.")
        finally:
            print("Do you want to continue...")

    else:
        break
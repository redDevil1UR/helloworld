car_running = False
while True:
    mp = input(">")
    if mp.lower() == "help":
        print('''start - to start the car 
stop - to stop the car 
quit - to exit''')
    elif mp == "start":
        if not car_running:
            car_running = True
            print("Car started...Ready to go!")
        else:
            print("Car's already started, what are you doing ?")
    elif mp == "stop":
        if car_running:
            car_running = False
            print("car stopped.")
        else:
            print("car was not running, cannot be stopped")
    elif mp == "quit":
        print("thank you for using this products")
        break
    else:
        # continue while loop
        print("I don't understand that...")

from datetime import datetime, timedelta
import time
import msvcrt

while True:
    print("\n---Life Counter Menu---")
    print("\n1.View life expectancy countdown")
    #print("2.The days left of your life.")
    print("2.View total seconds remaining")
    print("3.View time you've already lived")
    print("4.Exit")

    choice = input("\nPlease choose an option 1 ~ 4 : ")

    if choice == "1":
        life_expectancy = int(input("\nPlease enter your expected lifespan (in years): "))
        birth_input = input("Please enter your birthday (YYYY.MM.DD): ")
        try:
            birth_date = datetime.strptime(birth_input, "%Y.%m.%d")
        except ValueError:
            print("Invalid date format. Please try again in YYYY.MM.DD!!")
            continue
        #birth_date = datetime.strptime(birth_input, "%Y.%m.%d")

        now = datetime.now()
        expected_death_date = birth_date + timedelta(days = life_expectancy * 365)
        time_left = expected_death_date - now
        seconds_left = int(time_left.total_seconds())

        print("\n( Press [enter] to stop counting down. )")

        expected_death_date = birth_date + timedelta(days = life_expectancy * 365)
        days_left = (expected_death_date - now).days
        print(f"\n~~You still have approximately {days_left} days left~~\n")

        while seconds_left > 0:
            years = seconds_left // (365 * 24 * 60 * 60)
            days = (seconds_left % (365 * 24 * 60 * 60)) // (60 * 60 * 24)
            hours = (seconds_left % (60 * 60 * 24)) // (60 * 60)
            minutes = (seconds_left % (60 * 60)) // (60)
            seconds = seconds_left % 60
            
            #print(f"Time remaining: {years} years {days} days {hours} hours {minutes} minutes {seconds} seconds", end = "\r", flush = True)
            msg = f"~~Time remaining → {years} years {days} days {hours} hours {minutes} minutes {seconds} seconds"
            print(f"\r{msg:<65}", end = "", flush = True)
             
            time.sleep(1)
            seconds_left -= 1

            if msvcrt.kbhit():
                key = msvcrt.getwch()
                if key == "\r":
                    print("!Stop!")
                    break
    #combined to choice 1
    #elif choice == "2":
    #    life_expectancy = int(input("\nplease enter your expected lifespan (in years): "))
    #    birth_input = input("please enter your birthday (YYYY.MM.DD): ")
    #   try:
    #        birth_date = datetime.strptime(birth_input, "%Y.%m.%d")
    #    except ValueError:
    #        print("Invalid date format. Please try again in YYYY.MM.DD!!")
    #        continue
        #birth_date = datetime.strptime(birth_input, "%Y.%m.%d")

    #    now = datetime.now()
    #    expected_death_date = birth_date + timedelta(days = life_expectancy * 365)
        
    #    days_left = (expected_death_date - now).days
    #  print(f"\nyou still have approximately {days_left} days left.")

    elif choice == "2":
        life_expectancy = int(input("\nplease enter your expected lifespan (in years): "))
        birth_input = input("please enter your birthday (YYYY.MM.DD): ")
        try:
            birth_date = datetime.strptime(birth_input, "%Y.%m.%d")
        except ValueError:
            print("Invalid date format. Please try again in YYYY.MM.DD!!")
            continue
        #birth_date = datetime.strptime(birth_input, "%Y.%m.%d")

        now = datetime.now()
        expected_death_date = birth_date + timedelta(days = life_expectancy * 365)
        seconds_left = int((expected_death_date - now).total_seconds())
        
        print("\n( Press [enter] to stop counting down. )")
        while seconds_left > 0:
            
            msg = f"Time remaining: {seconds_left} seconds."
            print(f"\r{msg}", end = "", flush = True)
            time.sleep(1)
            seconds_left -= 1


            if msvcrt.kbhit():
                key = msvcrt.getwch()
                if key == "\r":
                    print(" !Stop!")
                    break
        
    elif choice == "3":
        birth_input = input("Enter your birthday(YYYY.MM.DD): ")
        try:
            birth_date = datetime.strptime(birth_input, "%Y.%m.%d")
        except ValueError:
            print("Invalid date format. Please try again.")
            continue
        
        
            
        now = datetime.now()
        days_passed = now - birth_date
        seconds_alive = int(days_passed.total_seconds())

        print("\n( Press [enter] to stop counting down. )\n")

        while seconds_alive > 0:       
            years = seconds_alive // (365*24*60*60)
            days = (seconds_alive % (365 * 24 * 60 * 60)) // (60 * 60 * 24)
            hours = (seconds_alive % (60 * 60 * 24)) // (60 * 60)
            minutes = (seconds_alive % (60 * 60)) // (60)
            seconds = seconds_alive % 60
            msg = f"You have been living: {years} years {days} days {hours} hours {minutes} minutes {seconds} seconds"
            print(f"\r{msg:<65}", end = "", flush = True)
            time.sleep(1)
            seconds_alive -= 1
            #\r means return to the head of sentence
            
            if msvcrt.kbhit():
                
                key = msvcrt.getwch()
                if key == "\r":
                    print("!Stop!")
                    break

    
    elif choice == "4":
         print("...")
         time.sleep(1)
         print("...")
         time.sleep(1)
         print("Good bye!! Remember to live meaningfully!!")
         time.sleep(4)
         break


    elif choice == "jookerej":
        print("...")
        time.sleep(1)
        print("omedetou")
        time.sleep(2)
        print("and")
        time.sleep(1)
        print("sayonara...")
        time.sleep(3)
        

    else:
         print("\nInvalid option. Please choose 1 ~ 4 !" + "\n")
         

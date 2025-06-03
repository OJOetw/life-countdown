from datetime import datetime, timedelta
import time
import msvcrt

while True:
    print("\n---Life Counter Menu---")
    print("\n1.Life Expectancy.")
    print("2.The days left of your life.")
    print("3.The seconds left of your life.")
    print("4.How long have you benn living.")
    print("5.Exit")

    choice = input("\nPlease choose an option 1 ~ 5 : ")

    if choice == "1":
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
        time_left = expected_death_date - now
        seconds_left = int(time_left.total_seconds())
        

        #years_left = life_expectancy - current_age
        #days_left = years_left * 365
        #hours_left = days_left * 24
        #minutes_left = hours_left * 60
        #seconds_left = minutes_left * 60

        print("\n( Press [enter] to stop counting down. )")

        while seconds_left > 0:
            years = seconds_left // (365 * 24 * 60 * 60)
            days = (seconds_left % (365 * 24 * 60 * 60)) // (60 * 60 * 24)
            hours = (seconds_left % (60 * 60 * 24)) // (60 * 60)
            minutes = (seconds_left % (60 * 60)) // (60)
            seconds = seconds_left % 60
            
            #print(f"Time remaining: {years} years {days} days {hours} hours {minutes} minutes {seconds} seconds", end = "\r", flush = True)
            msg = f"Time remaining: {years} years {days} days {hours} hours {minutes} minutes {seconds} seconds"
            print(f"\r{msg:<65}", end = "", flush = True)     
            time.sleep(1)
            seconds_left -= 1

            if msvcrt.kbhit():
                key = msvcrt.getwch()
                if key == "\r":
                    print("Stop!")
                    break
                        
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
        
        days_left = (expected_death_date - now).days
        print(f"\nyou still have approximately {days_left} days left.")

    elif choice == "3":
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
                    print(" Stop!")
                    break
        
    elif choice == "4":
        birth_input = input("Enter your birthday(YYYY.MM.DD): ")
        try:
            birth_date = datetime.strptime(birth_input, "%Y.%m.%d")
        except ValueError:
            print("Invalid date format. Please try again.")
            continue
        
        
            
        now = datetime.now()
        days_passed = now - birth_date
        seconds_alive = int(days_passed.total_seconds())
        
        years = seconds_alive // (365*24*60*60)
        days = seconds_alive // (24*60*60)
        hours = seconds_alive // (60*60)
        seconds = 
        print(f"You have been alive for {seconds_alive} days")
        

    
    elif choice == "5":
         print("...")
         time.sleep(1)
         print("...")
         time.sleep(1)
         print("Good bye!! Remember to live meaningfully!!")
         time.sleep(4)
         break


    elif choice == "jookerej":
        print("...")
        time.slepp(1)
        print("omedetou")
        time.sleep(2)

    else:
         print("\nInvalid option. Please choose 1 ~ 4 !" + "\n")
         

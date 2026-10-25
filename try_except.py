while True:
    try:
        age = int(input("Enter your age: "))
        print(f"You are {age} years old")
        break
    except ValueError:
        print("❌ Please enter a number!")

while True:
    try:
        number = int(input("Enter a number: "))
        result = 100 / number
        
    except ValueError:
        print("Thats not a valid number!")

    except ZeroDivisionError:
        print("You cannot divide by zero!")

    except:
       print("Error")

    else:
        print(f"Result: {result}")
        break

    finally:
        print("Program Finished")

#while True:
    #number = input("Enter a number: ")
    #result = 100 / number
    #if type(number)!= int:
     #   raise ValueError-"Thats not a valid number!"
    #else:
      #  print(f"Result: {result}")
        # break
          #raise ZeroDivisionError ("You cannot divide by zero!")

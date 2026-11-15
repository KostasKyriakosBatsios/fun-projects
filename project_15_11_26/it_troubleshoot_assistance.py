def main():
    print("=========================\nIT TROUBLESHOOT ASSISTANT\n=========================")
    ans = int(input("\nSelect your problem:\n\n1. Internet Connection\n2. Printer Problem\n3. Login Problem\n\nYour choice: "))
    get_answer(ans)
    

def get_answer(n):
    match n:
        case 1:
            q = input("\nIs it connected to the Wi-Fi?\n- ").strip().lower()
            if q == "no":
                print("\nEnable Wi-Fi and connect!")
            elif q == "yes":
                print("\nCheck the router or try another website!")
            else:
                print("\nPlease choose either yes or no!")
        case 2:
            q = input("\nIs the printer on?\n- ").strip().lower()
            if q == "no":
                print("\nTurn on the printer.")
            elif q == "yes":
                print("\nCheck the connection and paper!")
            else:
                print("\nPlease choose either yes or no!")
        case 3:
            q = input("\nIs the password correct?\n- ").strip().lower()
            if q == "no":
                print("\nPlease check the password!")
            elif q == "yes":
                print("\nCheck the keyboard (especially the Caps Lock) or contact the admin!")
            else:
                print("\nPlease choose either yes or no!")
        case _:
            print("\nInvalid selection. Please choose 1, 2 or 3.")


main()

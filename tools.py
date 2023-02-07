#This python file consists functions that help with developing and testing.
import os
def refresh():
    if os.path.exists("website/database.db"):
        os.remove("website/database.db")
    else:
        print("The file doesn't exist")
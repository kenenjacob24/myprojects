def shutdown(answer):
    if answer.lower() == 'yes':
        print("Shutting down the system...")
        # Code to shut down the system would go here
    else:
        print("Shutdown canceled.")

answe = input("Do you want to shut down the system? (yes/no): ")
shutdown(answe)
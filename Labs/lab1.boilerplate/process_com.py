import os
import sys
import math

def A(y):
    """Computes and returns the sum of 0 + 1 + 2 + 3 + ... + k + ... + [y/2]"""
    total = 0
    for i in range(int(y/2) + 1):
        total += i
    return total

def B(y):
    """Computes the sum of [(y/2)+1] + [((y+1)/2)+1] + [((y+2)/2)+1] + ... [((y+k)/2)+1] + ... + y"""
    total = 0
    for i in range(int(math.floor(y/2)+1), y+1):
        total += i
    return total

def main(n = None):
    Total = 0

    # Check for the correct number of command-line arguments
    if n is None:
        print("The program needs one parameter to be executed (e.g., python_script.py 13)")
        sys.exit(0)

    x = n

    """Added this parameter check because of my cli implementation"""
    # check if x is a valid integer
    if x.lstrip('-+').isdigit() == False:
        print("Unvalid parameter: The parameter should be an integer, exiting ...")
        sys.exit(0)
    else:
        x = int(x)

    # Ensure that the parameter is greater than 0
    if x <= 0:
        print("Unvalid parameter: The parameter should be greater than 0, exiting ...")
        sys.exit(0)

    # Create a child process
    pid = os.fork()

    # If the fork failed
    if pid < 0:
        print("Fork system call failed")
        return

    if pid != 0:  # Parent process
        # Wait for the child process to terminate
        exit_value = os.wait()

        # Get the child process's exit status
        child_process = os.WEXITSTATUS(exit_value[1])

        Total += A(x)
    else:  # Child process
        Total += B(x)
        os._exit(Total)  # Ensure the child process terminates here

    # If this is the parent process, print the total summation
    if pid != 0:
        # Get the child process's exit status
        Total += child_process

        print(f"The total is: {Total}")

        # Added this print statement to show the expected value
        # print(f"Expected Value: {A(x)} + {B(x)} = {A(x) + B(x)}")

if __name__ == "__main__":
    # default code 
    """ 
    n = 1
    main(n)
    """

    # replaced with command line arg implementation
    main(sys.argv[1] if len(sys.argv) > 1 else None)


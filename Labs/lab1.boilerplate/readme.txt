CISC 324 - Operating Systems
Lab #1
Hashir Sami

Pretext:
I modified the original code by actual CLI to the code implementation. you will need to run it in terminal to input the arguments necessary.
(i.e. cd ../../../dir && python process_com.py 14)

1. Compile and execute the program for different values of n. The program appears to be returning incorrect computations (e.g., for 𝑛 = 1 it returns 0). Why is that?

    The reason this occurs is because the parent process does not wait for the child processes' calculations to finish. As a result, they are not accounted for in the final computation. For example, for n = 0:

    A(x) returns 0
    B(x) returns 1

    Without the error, our calculation A(x) + B(x) would return 1. However, since the child process, which in this case is the process that executes B(x), is not accounted for by the parent process, the computation is incorrect.

2. Modify the program code to fix the issue using “wait()” and exit() system calls. Explain how you
fixed the issue.

    I fixed this issue by modifying code like this:

    In the parent process Total calculation, I added this piece of code:
        # Wait for the child process to terminate
        exit_value = os.wait()

        # Get the child process's exit status
        child_process = os.WEXITSTATUS(exit_value[1])
    
    In the child process Total calculation, I modified the exit code:
        os._exit(Total)  # Ensure the child process terminates here

    Finally, in the parent process Total printing, I added this piece of code:
        # Get the child process's exit status
        Total += child_process

    This resolved the issue because it forced the parent process to wait for its' child processes calculations to finish. After finishing the process, the exit status of the child process was the total value B(x) would produce. Using the exit value of the process, we assigned this to the child_process variable and then added it into our Total in the parent process. This solves our error while following the initial guidelines of having the parent process print the final solution.

3. After fixing the issue, you may notice that starting from a certain value of n, the returned sum
becomes incorrect. What is that value of n? Explain the reason behind this limitation.

    Starting at n = 26, the returned sum becomes incorrect. The reason this occurs is because of the limitations of the OS exit status. At max, the OS exist status can be 255, as it is stored as an 8-bit integer. When n is 26, A(x) returns 91 and B(x) returns 260. Therefore, when the child process tries to exit with 260, it returns 4 instead (wraps around the integer). This results with the total being 95 rather than 351. 

4. If we switch the function of the parent and child process (i.e., A(.) by B(.) and B(.) by A(.) in the
source code), you may still notice that starting from a certain value of n, the returned sum
becomes incorrect. What would be that value of n?

    By switching the function of the parent and child process, the returned sum becomes incorrect at n = 46. Similarly to the original problem, this occurs because of the limitations of the OS exit status. When n is 46, the value of B(x) is 805 and the value of A(x) is 276. Because A(x) is now occurring in the child process, and exit statuses have a limit of 255, the 276 is wrapped around and returns 20 instead. This results in the output of 825 instead of 1081.


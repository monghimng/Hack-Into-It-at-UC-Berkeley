# Hack-Into-It-at-UC-Berkeley
This command line tool helps recently graduated college students determine their expected job salary based on their prospective career field and geographical location. By comparing expected job salaries for various combinations, the user should be able to determine the career field and job location that is right for them and meets their salary interests.

First, the user is asked to input their career field of interest and the state in which they want to live by entering numbers from menu lists. Then, based on the choices, we access US Census data for the career field and state they choose, which returns a list of median salaries for the career field in the state.

To process the data, we use a linear regression model to find the average of the salaries. We output the average to the user as their expected salary and also a graphical distribution of all of the salaries. 

To use this tool. First install Python3. Then run "python3 main.py" in the commmand line in this current directory.

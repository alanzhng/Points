# Usage

This project was developed in VS Code. To set up Python scripts in VS Code, follow the steps of this tutorial: https://code.visualstudio.com/docs/python/python-tutorial.

<br/>

To run this script, navigate to the working directory. Then run the following command in the terminal where `<PTS_TO_SPEND>` is the amount of points that should be spent after reading in all transactions.

```
python3 script.py <PTS_TO_SPEND>
```
Given valid arguments, this script returns a dictionary of all payers' point balances for a single user.

<br/>

All transactions are read from `transactions.csv`. This file can be modified to change the transactions the script operates on.

# Comments

I assumed users of this script are aware of the function and background outlined in the Coding Exercise document. 
Thus, I made assumptions in writing this program. Some of these assumptions include that command line arguments are integers and that transactions in `transactions.csv` make mathematical sense. 
If I were developing this program as a real product, there are a number of improvements I could make, such as handling these edge cases, creating a UI, etc.

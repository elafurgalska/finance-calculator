Finance Calculators


This Python program provides two financial calculators: an investment calculator and a home loan repayment calculator. The user can choose between these options and perform calculations based on their inputs.

1. Getting Started

Clone the repository to your local machine:
git clone https://github.com/your-username/finance_calculators.git
cd finance_calculators

The program uses the math library and nothing else. So, as long as you have python installed, you should be ok. To double check you have python installed run the following command:

python

If you do have it installed, you will get details of your version. If you don't have it installed, install the correct package directly from the Python.org website.

2. Run the program

Either open the file using your usual code editor, or prompt your machine to do so in the terminal, using the following command:

python finance_calculators.py

3. Usage

Upon running the program, the user will be prompted to choose between the investment and bond calculators. The program recognises various inputs for the choice, such as 'investment', 'Investment', 'INVESTMENT', 'bond', 'Bond', 'BOND', etc.

- Investment Calculator
If the user selects 'investment', they will be asked to input:

The amount of money deposited.
The interest rate (as a percentage, without the '%').
The number of years for the investment.
Whether they want "simple" or "compound" interest.
The program will then calculate and print the amount the user will get back after the specified period, at the specified interest rate.

- Bond Calculator
If the user selects 'bond', they will be asked to input:

The present value of the house.
The interest rate.
The number of months they plan to take to repay the bond.
The program will then calculate and print the monthly repayment amount for the home loan.

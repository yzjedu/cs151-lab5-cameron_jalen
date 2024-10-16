# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
1. Set constant of the variable "balance" to 1000
2. Set action to "g"
3. set sentinel to 'e'
4. Create a while loop, while the user's action is not equal to the sentinel
   1. Prompt user for which action they'd like to do: withdraw (w), deposit (d), view balance (v), or exit (e)
         1. Type cast user's answer to all lowercase characters.
         2. if user action is "w"
            1. prompt user for how much they'd like to withdraw using the variable "amount"
            2. if "amount" is less than 0
                  1. output "You can't deposit a negative amount"
               else
                  2. update the "balance" variable by subtracting the "amount"
                  3. if "balance" is less than 0
                     1. output "You will be charged 5% interest"
            3. output the user's balance
         3. if user action is "d"
            1. prompt user for how much they'd like to deposit using the variable "amount"
            2. while "amount" is less than 0
               1. output "That is not a valid amount, enter a new amount."
               2. prompt user for how much they'd like to deposit
            3. update the "balance" variable  by adding the "amount"
            4. output the user's balance
         4. if user action is "v"
            1. output the "balance" variable
5. if the user's action is equal the sentinel
   1. output "Have a good day!"
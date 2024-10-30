# Goldbach_Conjecture_Pairs

Creates a list with Golbach pairs primes for the Nth number.

This started because my dad, who's a math teacher, ask me to write a program to get the pair prime for any N even number.

I wrote the algorithm because my father randomly present me this problem and I found it interesting and easy to solve by brute force recursion.
so in less than 10 minutes I explained to him the solution . you got the N number, You take a list of primes that is the closest and less than the N number(is never equal to N because it is even) .
You take this prime, store it on a list "Pairs" rest it from N , and do the same operation with the rest number.. you take the closest < prime , store it on the Pair list and rest it... at this point if you got 0 rest, you got your pair!, if not you start over,   , you.. if you got another rest then your first prime chosen is no good so you take the next one closest and less than N
and start the process over.

The implementation took me over 2 weeks to be ready and fast?, still take a lot for big N. also I added a recursive function that uses the base pair function to output all pairs to the N number..which was what actually my father wanted. 

I also tracked how many recursions the program took to solve each pair, this list outputs integers that grow very little even on big N...interesting.

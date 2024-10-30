# Goldbach_Conjecture_Pairs

Creates a list with Golbach pairs primes for the Nth number.
this started because my dad, whoa math teacher, ask me to write a program to get the prime pair for any N pair.

I wrote the algorithm because my father randomly present me this problem and I found it interesting and easy to solve by brute force recursion.
so in less than 10 minutes I explain him the solution . you got the N number, You take a list of primes that is the closest but < than the N number.
You take this prime, sotre it on a list "Pairs" rest it from N , and you do the same operation with the rest you got.. you take the closest < prime , store it on the Pair list and rest it... at this point if you got 0 rest, you got your pair!, if not you start over,   , you.. if you got another rest then your first prime choosen is no good so you take the next one closest and less than N
and start the process over.
The implementation took me over 2 weeks to be ready and fast?, still take a lot for big N. also I added a recursive function that use the base pair function to output all pairs to the N number..
which was actually what my father wanted. 
I also tracked how many recursions the program takes to solve each pair, this list outputs integers that grow very little even on big N, maybe the solution to the mystery of why there is always a goldbach prime pair for each even number .



Is very simple, it compares

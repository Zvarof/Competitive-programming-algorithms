/*

& : If both 1 -> 1                  else 0 
| : If either 1 -> 1                else 0
^ : If one 1 and the other 0 -> 1   else 0
~ : Set the complement : set -> clear ; clear -> set
>> x : Shift the bit to the right (x times) [Equivalent to dividing it by 2**n]
<< x : shift the bit to the left (x times) [Equivalent to multiplying it by 2**n]

*/

// Setting the x-th bit in a number n
n | (1 << x);
// Flip the x-th bit in a number n
n ^ (1 << x);
// Clear the x-th bit in a number n
n & ~ (1 << x);

// Check if a bit is set
bool is_set(unsigned int number, int x){
    return (number >> x) & 1;
}

// Check if an integer is a power of 2
bool isPowerOfTwo(unsigned int n){
    return n && !(n & (n-1));       // different de 0 et aucun bit en commun
}

// Clear the most-right set bit
n = n & (n-1);

// Clearing all trailing ones
n = n & (n+1);

// Counting the number of bit set
int counSetBits(int n){
    int count = 0;
    while (n)
    {
        n = n & (n-1);
        count ++ 
    }
    return count;
}




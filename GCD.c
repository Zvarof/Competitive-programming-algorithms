// Case 1 : If both a and b are even -> GCD (2a, 2b) == 2*GCD(a, b)
// Case 2 : If a is even and b is odd -> GCD (2a, b) == GCD(a, b)
// Case 3 : If both a and b are odd -> GCD (a, b) == GCD (b, a-b)    (Where b > a)

/* 
Note that Case 1 is True because :
    if both a and b are even, then a/2 and b/2 are also integers
Note that Case 2 is True because : 
    
*/

int GCD(int a, int b){
    if (!a || !b)                                   // Check if either a or b == 0
        return a | b;                               // Return the number that is not 0
    unsigned shift = builtin_ctz(a | b);            // The number of commmon trailing 0 (ctz) between a and b [Case 1]
    a >>= __builtin_ctz(a);                         // Divise a by 2 until odd (no more trailing 0)
    do {
        b >>= __builtin_ctz(b);                     // Divise a by 2 until odd (no more trailing 0) [Case 2]
        if (a > b)
            swap (a, b);                            // Make sure that a < b is always true before b -= a
        b -= a;                                     // [Case 3]
    } while (b);
    return a <<= shift;                             // Return a multiplied by 2**shift
}
## Calculating the numbers of pertumatations consisting of P elements from a set containing N elements.

### Calculating all possible combination of n elements from a set of N elements.

## C++
unsigned long long factorial(int n) {
  if (n <= 0) : return 0;
  unsigned long long result = 1;
  for(int i=2; i<=n; i++){
    result *= i;
  return result;
}

## Python

def CombinationOfNfromN():
  if n <= 0: return 0
  result, i = 1, 2
  for i in range(2, n+1):
    result *= i
  return result

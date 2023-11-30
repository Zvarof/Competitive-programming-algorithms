## Calculating the numbers of pertumatations consisting of P elements from a set containing N elements.

### Calculating all possible combination that includes all the elements from a set.

## C++
unsigned long long factorial(int n) {
  if (n <= 0) : return 0;
  unsigned long long result = 1;
  for(int i=2; i<=n; i++){
    result *= i;
  return result;
}

## Python

def CombinationOfNfromN(n):
  if n <= 0: return 0
  result, i = 1, 2
  for i in range(2, n+1):
    result *= i
  return result

### Calculating all possible combination of P elements from a set of size N

## C++

unsigned long long combinations(int N, int P) {
  if (P<0 || P>N) {
    return 0;
  }

  unsigned long long result = 1;

  for (int i=1; i<=P; i++){
    result *= N--;
    result /= i;
  }
  return result;
  

## Python

import math
def Combination_P_from_N():
  return math.comb(N, P)


### Calculating all possible subsets (including null subset) from a set of size N

## C++

unsigned long long Combinations_Subsets_From_N(int N){
    unsigned long long result = pow(2, N);
    std::cout << result << std::endl;
    return result;
}

## Python

def Combination_Subsets_from_N(N):
    return 2**N

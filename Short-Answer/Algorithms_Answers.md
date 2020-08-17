#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)   a = 0 # 0(1) constant because its hard coded
    while (a < n * n * n): # 0(n) because its a loop and performs one operation
      a = a + n * n

      final answer
      # o(n)


b) sum = 0  - # 0(1) constant because its hard coded
    for i in range(n): # 0(n) because its a loop and performs one operation
      j = 1
      while j < n: # 0(n) because its a loop and performs one operation
        j *= 2
        sum += 1

        but because it is two loops, we add 2 because its performing two identical operations.

        final answear: 0(n^2)


c) def bunnyEars(bunnies):
      if bunnies == 0: - 0(n) is worst case because you are checking against a constant 
        return 0

      return 2 + bunnyEars(bunnies-1) # we don't what the input size is and it stops at the base case.
      
      o(n)

## Exercise II

divide floors by halves
  start at middle floor to see if that breaks the egg.
  if that floor does not break the egg, go to middle of the upper half
  if the egg does breaks at the current middle floor, go to the middle floor of the lower half
  repeat that to find the highest floor without the egg breaking

time complexity

0(log n)

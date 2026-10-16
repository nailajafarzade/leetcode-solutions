class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result=[]
        for x in range(1,n+1):
            if x%5==0 and x%3==0:
                result.append("FizzBuzz")
            elif x%3==0:
                result.append("Fizz")
            elif x%5==0:
                result.append("Buzz")
            else:
                result.append(str(x))
        return result
        
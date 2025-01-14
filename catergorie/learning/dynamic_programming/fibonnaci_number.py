class Learning:
    def fibonacci(self, n: int, depth=0):
        # Add logging to show the current call stack
        indent = "  " * depth  # Indent to represent recursion depth
        print(f"{indent}Calculating Fibonacci({n})")

        # Base case: return n if n is 0 or 1
        if n <= 1:
            print(f"{indent}Base case reached: Fibonacci({n}) = {n}")
            return n

        # Create a new instance of Learning (not necessary, but keeping your structure)
        l = Learning()

        # Recursive calls
        print(f"{indent}Splitting into: Fibonacci({n-1}) + Fibonacci({n-2})")
        result_n1 = l.fibonacci(n - 1, depth + 1)  # Fibonacci(n-1)
        result_n2 = l.fibonacci(n - 2, depth + 1)  # Fibonacci(n-2)

        # Combine results
        result = result_n1 + result_n2
        print(f"{indent}Result of Fibonacci({n}): {result}")
        return result


# Instantiate the class and calculate Fibonacci(10)
l = Learning()
print("Final Result:", l.fibonacci(10))

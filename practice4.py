# %% Cell 1
a = 5
b = 7
# %% Cell 2
result = a + b
print(result)


# %% Cell 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# %% Cell 2
result = factorial(5)
print(result)

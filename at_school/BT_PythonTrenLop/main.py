def myfunc(n):
    print(n)
    return lambda a: a * n


mydoubler = myfunc(2)(11)
# print(mydoubler(11))
print(mydoubler)

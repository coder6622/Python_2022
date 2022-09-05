# TODO: ham nac danh lambda
# TODO: labda: expression
def test(f, x, y):
    return f(x, y)


# Ham de quy luc nao cung co 2 thanh phan:
# Thanh phan dung
# Thanh phan de quy

def giaiThua(n):
    result = 1
    if n == 0:
        return 1

    return n * giaiThua(n - 1)


print(giaiThua(997))

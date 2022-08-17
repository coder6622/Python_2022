# a. Dao nguoc chuoi

# a = "Xuan Hung"[::-1]
# print(a)

b = "Hoang Long"


def reverse(s):
    s = "".join(reversed(s))
    return s


#

# print(reverse(b))


# b> Dao nguoc cac tu trong chuoi

c = "Cong nguyen"


def reverseWordInStr(s):
    result = ''
    tam = s.split()
    for j in range(len(tam)):
        # print(tam[i])
        reverse(tam[j])
        # var =

    print(tam)


reverseWordInStr(c)

# c. Kiem tra mot chuoi co doi xung hay khong
d = 'maiairm'


def KTDoiXung(s):
    giua = int(len(s) / 2)
    print(giua)
    if len(s) % 2 == 0:
        left = s[:giua]
        right = s[giua:][::-1]
    else:
        left = s[:giua]
        right = s[giua + 1:][::-1]

    if left == right:
        print('true')
    else:
        print('false')


def KTDoiXung2(s):
    n = len(s)


KTDoiXung(d)
KTDoiXung2(d)


def demTSXuatHien(word, s):
    count = 0
    for i in range(len(s)):
        if word == s[i]:
            count += 1

    return count


def arere(*args):
    print(args)


arere('12323', 'dfdfd', 3)

print(demTSXuatHien('a', d))


class Person:
    name = 'hello'
    __age = 20

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.__age)


class Hung(Person):
    def getName(self):
        super().getName()

    def getAge(self):
        super().getAge()


hung = Hung()
hung.getName()
hung.getAge()

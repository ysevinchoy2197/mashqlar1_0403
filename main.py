#1-misol
def a(son):
    if son > 0:
        return "Musbat"
    else:
        return "Manfiy yoki nol"

x = -10
res = a(x)
print(f"{x} soni {res}")

y = 27
res = a(y)
print(f"{y} soni {res}")

#2-misol
def a(son):
    if son > 0:
        return True
    else:
        return False
x = 2
res = a(x)
print(f"{x} soni {res}")

y = 1
res = a(y)
print(f"{y} soni {res}")

#3-misol
def b(son):
    if son > 100:
        return "Katta"
    else:
        return "Kichik"

x = 101
res = b(x)
print(f"{x} soni {res}")

#4-misol
def sonlar(a, b):
    if a == b:
        return "Teng"
    else:
        return "teng emas"

x = 3
res = sonlar(x, x)
print(f"{x} soni {res}")

res = sonlar(x, x)
print(f"{x} soni {res}")


#5-misol
def yoshlar(yosh):
    if yosh >= 18:
        return "Ruxsat berildi"
    else:
        return "Ruxsat berilmadi"

x = 14
res = yoshlar(x)
print(f"{x} soni {res}")

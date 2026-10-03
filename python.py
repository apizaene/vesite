# 1. Тааныштыруу. Атыңды жана шаарыңды сура, «Салам, Айбек! Сен Ош шаарынан экенсиң» деп чыгар.
# aty = input("Атың ким? ")
# shaary = input("Кайсы шаардансың? ")
# jashyn = int(input("Жашың? "))
# print(f"Салам, {aty}! Сен {shaary} шаарынан экенсиң. Жашың {jashyn} Кийинки жылы {jashyn} + 1\n")



# 2. Кошуучу. Эки санды сура, алардын суммасын, айырмасын жана көбөйтүндүсүн көрсөт.
# a = float(input("Биринчи сан: "))
# b = float(input("Экинчи сан: "))

# print(f"Суммасы (+):", a + b)
# print(f"Айырмасы: (-)", a - b)
# print(f"Көбөйтүндүсү: (*)\n", a * b)



# 3. Тик бурчтук. Узундугу менен туурасын сура, аянтын (a*b) жана периметрин (2*(a+b)) эсепте.
# uzunu = float(input("Узуну: "))
# tuurasy = float(input("Туурасы: "))

# ayanty = uzunu * tuurasy
# perimetr = 2 * (uzunu + tuurasy)

# print("Аянты (a * b):", uzunu)
# print("Периметри (2 * (a + b)):", perimetr)



# 4. Убакыт. Секунд санын сура, канча саат, минута жана секунд экенин // жана % менен тап.
# second = int(input("Секунд саны: "))

# saat = second // 3600
# minuta = (second % 3600) // 60
# kalgan_sekund = second % 60

# print(f"{second} секунд = {saat} саат, {minuta} минута, {kalgan_sekund} секунд\n")

# print("Саат:", saat)
# print("Минута:", minuta)
# print("Секунд:", kalgan_sekund)



# # 5. Чакан кассир. Товардын баасын жана санын сура, жалпы сумманы чыгар. Бонус: 10% арзандатуу кош.
# baasy = float(input("Товардын баасы: "))
# sany = int(input("Саны: "))

# jalpy = baasy * sany
# arzandatuu = jalpy * 0.10
# tolo_summasy = jalpy - arzandatuu

# print(f"Жалпы сумма: {jalpy} сом")
# print(f"10% арзандатуу: {arzandatuu} сом")
# print(f"Төлөнүүчү сумма: {tolo_summasy} сом")



# # Колдонуучунун жашын суроо
# jash = int(input("Жашынызды киргизиниз: "))

# # Шартты текшеруу
# if jash >= 18:
#     print("Кирууго уруксат берилет!")
# else:
#     print("Кирууго уруксат жок!")



# ball = int(input("Топтогон балды киргизиниз: "))

# if ball < 0 or ball > 100:
#     print("Ката: Мындай балл болушу мумкун эмес! 0 менен 100дун ортосундагы сан жазыныз")
# elif ball >= 90:
#     print("Сиздин бааныз: 5 (Эн жакшы)")
# elif ball >= 75:
#     print("Сиздин бааныз: 4 (Жакшы)")
# elif ball >= 50:
#     print("Сиздин бааныз: 3 (Канааттандырарлык)")
# else:
#     print("Сиздин бааныз: 2 (Канааттандырарлык эмес, дагы аракет кылыныз)")




        # homework

# print("---Жуп жана так сан---")
# san = int(input("Бир сан жазыңыз: "))

# if san % 2 == 0:
#     print("Бул жуп сан")
# else:
#     print("Бул так сан")



# print("---Билет алуу---")
# jash = int(input("Жашыңызды жазыңыз: "))

# if jash < 7:
#     print("Сизге билет бекер! 👶")
# else:
#     print("Билеттин баасы 250 сом 🎟️")



# print("---Бутун жана так сан---")
# san = int(input("Бир бүтүн сан жазыңыз: "))

# if san > 0:
#     print("Бул оң (позитивдүү) сан 📈")
# elif san < 0:
#     print("Бул терс (негативдүү) сан 📉")
# else:
#     print("Бул нөл сан 0️⃣")



# print("---Пароль---")
# password = "python123"

# user_password = input("Паролду киргизиңиз: ")

# if user_password == password:
#     print("Купуя сөз туура! Кош келдиңиз 🎉")
# else:
#     print("Купуя сөз ката! ❌")



# aty ="user"
# parol = "12345"
# loginname = input("Логин жаз: ")
# loginparol = input("пароль жаз: ")
# if loginname == aty and loginparol == parol:
#     print("Кош келдин")
# elif loginname != aty and loginparol == parol:
#     print("Логин ката")
# elif loginname == aty and loginparol != parol:
#     print("Пароль ката")
# else:
#      print("Логин ката, Пароль ката")


# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# for i in range (10) :
#     if i == 5:
#         break
#     print (i)


# for i in range (5) :
#     if i == 2:
#         continue
#     print (i)

# for i in range (3) :
#     print (i)
# else:
#     print("Бутту")

# n = 6
# for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")

# marks = [5, 4, 3, 5, 4]
# total = 0
# for m in marks:
#     total += m
# print("Сумма:", total)
# print("Орточо:", total / len(marks))



# i = 1
# while i <= 5:
#     print(i)
#     i += 1


# for i in range(2, 31, 2):
#     print(i)

# for i in range(1, 31, 1):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)


# summa = 0

# for i in range(1, 11):
#     summa += i
# print(summa)


# --- 1 тапшырма ---
# for i in range(1, 11):
#     print(i)

# --- 2 тапшырма ---
# for i in range(10, 0, -1):
#         print(i)

# --- 3 тапшырма ---
# for i in range(2, 21, 2):
#     print(i)

# --- 4 тапшырма ---
# for i in range(1, 22, 2):
#     print(i)

# --- 5 тапшырма ---
# summa = 0

# for i in range(1, 11):
#     summa += i
# print(summa)

# --- 6 тапшырма ---
# n = int(input("n санын киргизиңиз: "))

# for i in range(1, n + 1):
#     print(i)

# --- 7 тапшырма ---
# n = int(input("сан киргизиңиз: "))
# for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")

# --- 8 тапшырма ---
# i = 1

# while i <= 10:
#     print(i)
#     i += 1

# # --- 9 тапшырма ---
# i = 10

# while i >= 1:
#     print(i)
#     i -= 1

# --- 10 тапшырма ---
# i = 2

# while i <= 20:
#     print(i)
#     i += 2

# --- 11 тапшырма ---
# while True:
#     n = int(input("Сан киргизиңиз: "))

#     if n == 0:
#         break

#     print (n)

# --- 12 тапшырма ---
# n = int(input("n санын киргизиңиз: "))

# i = 1
# summa = 0

# while i <= n:
#     summa += i
#     i += 1

# print("Суммасы:", summa)

# --- 13 тапшырма ---
# i = 1

# while i <= 50:
#     if i % 5 == 0:
#         print(i)
#     i += 1

# --- 14 тапшырма ---
# i = 1

# while i <= 100:
#     if i % 3 == 0:
#         print(i)
#     i += 1

# --- 15 тапшырма ---
# n = int(input("Сан киргизиңиз: "))

# san = abs(n)
# count = 0

# if san == 0:
#     count = 1
# else:
#     while san > 0:
#         san //= 10
#         count += 1

# print("Цифралардын саны:", count)



# Зеленый текст
print("\033[32mЭтот текст зеленый\033[0m")


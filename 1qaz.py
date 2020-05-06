import random
def ц ():
     print("Hello")
     р=input('Меня завут Android100500, a тебе : ' )
     print("Значить тебе звати " + р)
     print("Давай ми  порывнняэмо твоэ число бильше ли число за 67:")
     while True:
            try:
                  л = int (input (""))
                  if (л>67):
                        print("True")
                  else:
                        print("False")
            except ValueError as e:
                  print(e)
            except UnboundLocalError as e:
                  print("Вы ввели текст и число", e)
            else:
                  print("Все вырно")
            finally:
                print(л)
            break
     x = input("Веди текст: ")
     z = len (x)
     if z ==10:
         print("Вы вели "+ z +" символов")
     elif z < 10:
         print("Вы вели меньше 10 символов")
     else:
         print("Вы вели больше 10 символов")
         
     a = ['Кородко','Не','Знаю','Що','Тут','Написати','Тому','Я','Напишу','Цы','слова']
     print(a)
     del a[3]
     del a[7]
     print(a)
     a.insert(3,"Зачем")
     a.insert(7,"Вот цы слова")
     print(a)
     try:
          n = ("Давай сиграэм кубик Я кидаю ти выдгадуеш")
          d = random.randint(1,10)
          v = int(input("Угадай число "))
          if v == d:
                     print('Ти угадал')
          else:
                     print("Ти не угадал", d)
          o = ("Какой у тебя год")
          r = int(input())
          if (r % 4 == 0) and (r % 100 != 0) or (r % 400 == 0):
                     print("Yes")
          else:
                     print("No")
          j = " HACK "
          while " HACK " == " HACK ":
              print(j)
              j=j +" HACK "
          
     except ValueError :
                     print("Вы ввели текст")
     else:
                     ("Все вырно")
     finally:
                print("")
    
ц()




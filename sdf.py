class Робочи_дни():

      def Pon(pon):
             print("""   Урок  : Година  :  Оцынка
Физика     08:00          8
Инф.мат    08:50        10
Укр.лит      09:30        11
Укр.мова   10:15          5
Химия        12:00         7
   """)
      def Viv(der):
             print("""   Урок  : Година  :  Оцынка
Фыз.кул    08:00         12
Алгебра     08:50          7
Геомет       09:30          4
Географ    10:15           6
Муз.мист   12:00          11
   """)
      def Cer(cer):
             print("""   Урок  : Година  :  Оцынка
Фыз.кул    08:00         12
Алгебра     08:50          7
Геомет       09:30          4
Географ    10:15           6
Муз.мист   12:00          11
   """)

      def Cha(cha):
             print("""   Урок  : Година  :  Оцынка
Физика     08:00          8
Инф.мат    08:50        10
Укр.лит      09:30        11
Укр.мова   10:15          5
Химия        12:00         7
   """)
      def Pat(pat):
             print("""   Урок  : Година  :  Оцынка
Фыз.кул    08:00         12
Алгебра     08:50          7
Геомет       09:30          4
Географ    10:15           6
Муз.мист   12:00          11
   """)

Понедилок = Робочи_дни()
Вывторок = Робочи_дни()
Середа = Робочи_дни()
Четверг = Робочи_дни()
Пятниця = Робочи_дни()

z = input("Введите учебние дны:  ")
if (z == "Понедилок"):
     print(Робочи_дни.Pon(Понедилок))
if (z == "Вывторок"):
                print(Робочи_дни.Viv(Вывторок))
if (z == "Середа"):
                print(Робочи_дни.Cer(Середа))
if (z == "Четверг"):
                print(Робочи_дни.Cha(Четверг))
if (z == "Пятниця"):
                print(Робочи_дни.Pat(Пятниця))


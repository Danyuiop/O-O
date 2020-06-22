import random as rd
from random import randint, choices


class RT:
    def __init__(self, kiln):
        self.kiln = kiln


class RE:
    Kviti = RT(randint(15, 60))


class Muo:
    """
     ВУЕ
    """

    def __init__(self, vud, kilust):
        self.kilust = kilust
        self.FFF = []

    def so_ui(self):
        print(self.FFF)
        print(self.WE)

    def store_response(self, new_FFF, new_WE):
        self.FFF.append(new_FFF)
        self.WE.append(new_WE)

    def show_results(self):
        print("Скільки квітів: ")
        for FFF in self.FFF:
            print('-' + FFF)
        for WE in self.WE:
            print('-' + WE)

    def ispol(self):
        R4 = int(RE.Kviti.kiln)
        D4 = int(R4 // 2.4)
        P4 = R4 // 3.4
        C4 = R4 // 6
        V4 = R4 // 7

        S = D4 // 4
        E = D4 // 2
        e = D4 // 3
        print(S, E, e)
        pr = P4 // 2
        t = P4 // 1.75
        g = P4 // 10
        print(pr, t, g)
        k = C4 // 2
        y = C4 // 2.50
        l = C4 // 3
        print(k, y, l)
        h1 = V4 // 1.5
        h2 = V4 // 6.50
        h3 = V4 // 1.5
        print(h1, h2, h3)

        print(D4, P4, C4, V4, R4)
        print(D4 + P4 + C4 + V4)

        re = rd.choice(['Золоти', 'Жовтий', 'Блакитний'])
        yr = rd.choice(['Золоти', 'Жовтий', 'Блакитний'])
        et = rd.choice(['Золоти', 'Жовтий', 'Блакитний'])
        ree = "Всього"
        cg = rd.choice(['Likia', 'Troundu', 'Rotha', 'Orhidea'])
        vf = rd.choice(['Likia', 'Troundu', 'Rotha', 'Orhidea'])
        fr = rd.choice(['Likia', 'Troundu', 'Rotha', 'Orhidea'])
        print(re, yr, et)
        print("   " + str(S) + "       " + str(E) + "      " + str(e) + "       " + ":Надень народження")
        print("   " + str(int(pr)) + "       " + str(int(t)) + "      " + str(int(g)) + "       " + ":Просто так")
        print("   " + str(int(k)) + "       " + str(int(y)) + "      " + str(int(l)) + "       " + ":На косяк")
        print("   " + str(int(h1)) + "       " + str(int(h2)) + "      " + str(int(h3)) + "       " + ":На похорони")
        print("   " + cg + "      " + vf + "      " + fr + "     " + ":Квіті")
        print("--------Всього квытыв------------")

    def ispol(self):
        R4 = int(RE.Kviti.kiln)
        D4 = int(R4 // 2.4)
        P4 = R4 // 3.4
        C4 = R4 // 6
        V4 = R4 // 7

        S = D4 // 4
        E = D4 // 2
        e = D4 // 3
        pr = P4 // 2
        t = P4 // 1.75
        g = P4 // 10
        k = C4 // 2
        y = C4 // 2.50
        l = C4 // 3
        h1 = V4 // 1.5
        h2 = V4 // 6.50
        h3 = V4 // 1.5


        re = rd.choice(['Золоти', 'Жовтий', 'Блакитний'])
        yr = rd.choice(['Золоти', 'Жовтий', 'Блакитний'])
        et = rd.choice(['Золоти', 'Жовтий', 'Блакитний'])
        cg = rd.choice(['Likia', 'Troundu', 'Rotha', 'Orhidea'])
        vf = rd.choice(['Likia', 'Troundu', 'Rotha', 'Orhidea'])
        fr = rd.choice(['Likia', 'Troundu', 'Rotha', 'Orhidea'])
        print(re, yr, et)
        print("   " + str(S) + "       " + str(E) + "      " + str(e) + "       " + ":Надень народження")
        print("   " + str(int(pr)) + "       " + str(int(t)) + "      " + str(int(g)) + "       " + ":Просто так")
        print("   " + str(int(k)) + "       " + str(int(y)) + "      " + str(int(l)) + "       " + ":На косяк")
        print("   " + str(int(h1)) + "       " + str(int(h2)) + "      " + str(int(h3)) + "       " + ":На похорони")
        print("   " + cg + "      " + vf + "      " + fr + "     " + ":Квіті")
        print("--------Всього квытыв------------")
        print("          " + R4 + "             ")

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Ответі на вопроси:")
        for response in self.responses:
            print('- ' + response)

import random as rd


class kviti:
    def __init__(self, vid, kilkist):
        self.vid = vid
        self.kilkist = kilkist


class kviti2:
    lilia = kviti("Lilia", rd.randint(5, 15))
    rotha = kviti("rotha", rd.randint(5, 15))
    malivu = kviti("malivu", rd.randint(5, 15))
    troandu = kviti("troandu", rd.randint(5, 15))
    lipa = kviti("lipa", rd.randint(5, 15))


print(kviti2.lilia)


def comy(self, Col1, Col2, Col3):
    H = (
                self.lilia.kilkist + self.malivu.kilkist + self.rotha.kilkist + self.troandu.kilkist + self.lipa.kilkist) // 2
    C = (
                self.lilia.kilkist + self.malivu.kilkist + self.rotha.kilkist + self.troandu.kilkist + self.lipa.kilkist) // 4
    P = (
                self.lilia.kilkist + self.malivu.kilkist + self.rotha.kilkist + self.troandu.kilkist + self.lipa.kilkist) // 6
    R = (
                self.lilia.kilkist + self.malivu.kilkist + self.rotha.kilkist + self.troandu.kilkist + self.lipa.kilkist) // 8
    u = (
            self.lilia.kilkist + self.malivu.kilkist + self.rotha.kilkist + self.troandu.kilkist + self.lipa.kilkist)
    E = H // 1.9
    E1 = H // 4.3
    E2 = H // 3.4
    G = C // 3
    G1 = C // 2.20
    G2 = C // 3.10
    K = P // 2.4
    K1 = P // 3
    K2 = P // 3
    W = R // 2.5
    W1 = R // 1.5
    W2 = R // 7
    r = H + C + P + R
    T = E + G + K + W
    I = E1 + G1 + K1 + W1
    X = E2 + G2 + K2 + W2

    print(X, T, I, r)


    Color = Col1 + "  " + Col2 + "  " + Col3
    Kil = Col1 + "  " + Col2 + "  " + Col3
    D = Col1 + "  " + Col2 + "  " + Col3
    P = Col1 + "  " + Col2 + "  " + Col3
    C = Col1 + "  " + Col2 + "  " + Col3

    return Color.title()
    return Kil.title()
    return D.title()
    return P.title()
    return C.title()








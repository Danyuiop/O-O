from kviti import comy
import random as rd
import unittest as ut


class vgt(ut.TestCase):
    def test(self):
        GH = ["Green", "Red", "Golden" 'Blue', "Pink", "Yellow" "Wheeht", "Fiolet", "Red"]
        iop = rd.randint(0, len(GH) - 3)
        format_color1 = comy.Color({GH[iop]})
        Kilrty = comy.T + " " + comy.I + " " + comy.X
        print(vgt.format_color1)
        print(vgt.Kilrty)

        self.assertEqual(format_color1,
                         rd.choice(["Green", "Red", "Golden"], ["Blue", "Pink", "Yellow"], ["Wheeht", "Fiolet", "Red"]))


    if __name__ == '__main__':
        ut.main()


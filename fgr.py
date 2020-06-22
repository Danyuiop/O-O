import unittest
from kviti import Muo


class Tr(unittest.TestCase):

    def setUp(self):
        question = "Які квіти тобіподобаються"
        self.my_survey = Muo(question)
        self.responses = ['Золоти', 'Жовтий', 'Блакитний']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[1])
        self.assertIn(self.responses[1], self.my_survey.responses)

    def rew(self):
        Muo.ispol(str)




if __name__ == "__name__":
    unittest.main()
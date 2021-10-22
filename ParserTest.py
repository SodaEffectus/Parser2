import unittest
import robobas

str11 = "Добрый день высылаю линку https://github.com/omriharel/sd5223 вариант 0"
str12 = "Добрый день высылаю линку https://github.com/omriharel/sd6666 вариант 155"

class MyTestCase(unittest.TestCase):

    def test_Parser_link_est(self):

        self.assertEqual(robobas.get_link(str11), "https://github.com/omriharel/sd5223")

    def test_Parser_link_net(self):

        self.assertEqual(robobas.get_link(str12), "https://github.com/omriharel/sd6666")

    def test_Parser_variant_est(self):

        self.assertEqual(robobas.get_variant(str11), "вариант 0")

    def test_Parser_variant_net(self):

        self.assertEqual(robobas.get_variant(str12), "вариант 155")


if __name__ == '__main__':
    unittest.main()

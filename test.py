import unittest
import json
from cleanjason.print_neat_jason import Parsefile

#inherit Parsefile object, but have readinput changed, since we need to test on a local file.
class Parselocalfile(Parsefile):
    file=open('testdata.json',encoding='utf-8')

class MyTest(unittest.TestCase):
    def test(self):
        imputd=Parselocalfile().parse_by_chunk()
        diclist =[]
        for objs in imputd:
            diclist.append(objs)
        self.assertEqual(len(diclist),6)
        self.assertIn({"apple":"red"},diclist)
        self.assertIn({"orange":"yellow"},diclist)

if __name__ == '__main__':
    unittest.main()

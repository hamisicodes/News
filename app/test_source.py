import unittest
from  models import source


Source  = source.Source

class testSource(unittest.TestCase):
    def setUp(self):
        self.new_source  = Source("ke-news" , "Kenya News" , "Home of the latest kenyan news", "www.kenyanews.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source),Source)




if __name__ == '__main__':
    unittest.main()
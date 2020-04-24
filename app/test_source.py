import unittest
from  .models import source


Source  = source.Source

class testSource(unittest.TestCase):
    def setUp(self):
        self.new_source  = Source("ke-news" , "Kenya News" , "Home of the latest kenyan news", "www.kenyanews.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        self.assertEqual(self.new_source.id,"ke-news")
        self.assertEqual(self.new_source.name,"Kenya News")
        self.assertEqual(self.new_source.description,"Home of the latest kenyan news")
        self.assertEqual(self.new_source.url,"www.kenyanews.com")


if __name__ == '__main__':
    unittest.main()
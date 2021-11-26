import unittest
from unittest import TestCase
from regex import compare

class Test(TestCase):
    def test_comp_false(self):
        for s in [
            'colou+r|color',
            'col.+r$|colors',
                  'baa*|cab',
                  'colou?r|colouur',
            '^apple$|tasty apple',
            '^apple$|apple pie',
            'app$|apple',
            '^le|apple',
        ]:
            reg, inp = s.split('|')
            self.assertFalse(compare(reg, inp))

    def test_comp_true(self):
        for s in [
            'col.+r|collar',
                  '.$|apple',
                  'col.+r|collar',
                  'col.+r|colour',
                  'col.+r|color',
                  'col.+r|colr',
                  'colou*r|colouur',
                  'colou*r|colour',
                  'colou*r|color',
            'colou?r|color',
                  'colou?r|colour',
         '^app|apple',
         'le$|apple',
          '^a|apple',
          'apple$|tasty apple',
          '^apple|apple pie',
         '^apple$|apple']:
            reg, inp = s.split('|')
            self.assertTrue(compare(reg, inp))

# if __name__ == "__main__":
#     unittest.main()
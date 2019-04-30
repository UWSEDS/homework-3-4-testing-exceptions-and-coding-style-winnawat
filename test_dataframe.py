import unittest

import dataframe as dfpy
import hw2


class TestDataFrame(unittest.TestCase):

    def test_expectedcols(self):
        self.assertTrue(hw2.test_colnames(dfpy.data),
            msg='DataFrame does not contain expexted columns')

    def test_valuetypes(self):
        self.assertTrue(hw2.test_datatypes(dfpy.data),
            msg='DataFrame columns are not of expected datatypes')

    def test_no_nan(self):
        data = dfpy.data
        nancheck = data.isnull().any().any()
        self.assertFalse(nancheck, msg='DataFrame contains NaN')

    def test_leastonerow(self):
        data = dfpy.data
        rowcheck = False
        if data.shape[0] >= 1:
            rowcheck = True
        else:
            rowcheck = False
        self.assertTrue(rowcheck, msg='DataFrame has no row')

suite = unittest.TestLoader().loadTestsFromTestCase(TestDataFrame)
_ = unittest.TextTestRunner().run(suite)

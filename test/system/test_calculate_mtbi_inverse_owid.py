import unittest

import numpy as np
from numpy import testing
from src.data_manipulation.data_manager import DataManager
import src.interface.epydemics as ep


class CalculateMTBIInverseOWIDTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        DataManager.load_dataset('owid')

    def test_mtbi_inverses_owid_arg_from_1_to_40_starting_from_30(self):
        expected_inverses = np.power(np.array([0.0069, 0.0069, 0.0067, 0.0063, 0.0064,
                                               0.0064, 0.0065, 0.0066, 0.0067, 0.0066, 0.0067]), -1)
        mtbi_inverses = np.array(ep.calculate_mtbi_inverse('Argentina', dataset='total_cases', unit='day',
                                                           start=1, end=40, start_from=30, fit_x0=(0.1, 1),
                                                           formula='approx_conditional', output=False))
        testing.assert_allclose(expected_inverses, mtbi_inverses, rtol=0.1)

    def test_mtbi_inverses_owid_arg_from_40_to_80_starting_from_70(self):
        expected_inverses = np.power(np.array([0.0027, 0.0026, 0.0026, 0.0026, 0.0026,
                                               0.0026, 0.0025, 0.0025, 0.0025, 0.0025, 0.0025]), -1)
        mtbi_inverses = np.array(ep.calculate_mtbi_inverse('Argentina', dataset='total_cases', unit='day',
                                                           start=40, end=80, start_from=70, fit_x0=(0.1, 1),
                                                           formula='approx_conditional', output=False))
        testing.assert_allclose(expected_inverses, mtbi_inverses, rtol=0.1)

    '''
    def test_mtbi_owid_arg_50_days_from_30(self):
        expected_mtbis_day = np.array([0.0069, 0.0069, 0.0067, 0.0063, 0.0064,
                                       0.0064, 0.0065, 0.0066, 0.0067, 0.0066, 0.0067,
                                       0.0067, 0.0067, 0.0068, 0.0067, 0.0067, 0.0066,
                                       0.0066, 0.0067, 0.0067, 0.0067])
        mtbis = np.array(Fitter.calculate_mtbis('Argentina', dataset='total_cases',
                                                start=1, end=50, start_from=30, fit_x0=(0.1, 1),
                                                formula='approx_conditional'))
        testing.assert_array_almost_equal(expected_mtbis_day, mtbis, decimal=4)

    def test_mtbi_owid_arg_50_days_from_40(self):
        expected_mtbis = np.array([0.0067, 0.0067, 0.0067, 0.0068, 0.0067,
                                   0.0067, 0.0067, 0.0066, 0.0067, 0.0067, 0.0067])
        mtbis = np.array(Fitter.calculate_mtbis('Argentina', dataset='total_cases',
                                                start=1, end=50, start_from=40, fit_x0=(0.1, 1),
                                                formula='approx_conditional'))
        testing.assert_array_almost_equal(expected_mtbis, mtbis, decimal=4)
        '''

if __name__ == '__main__':
    unittest.main()
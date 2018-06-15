import unittest
from agilent4284a import Agilent4284A
from pyvisa.constants import StatusCode


def get_visaaddr():  # depends on environment. please modify here.
    return 'GPIB0::3::INSTR'


def get_id():  # depends on environment and instrument. please modify here.
    return 'HEWLETT-PACKARD,4284A,0,REV01.20\n'


class TestAgilent4284A(unittest.TestCase):

    def test_init(self):
        visa_addr = get_visaaddr()
        Agilent4284A(visa_addr)

    def test_get_id(self):
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result = lcr.get_id()

        self.assertEqual(result, get_id())

    def test_trigger_immediate(self):
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result = lcr.trigger_immediate()

        self.assertEqual(result[1], StatusCode.success)

    def test_set_frequency(self):
        freq = 500
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result = lcr.set_frequency(freq)

        self.assertEqual(result[1], StatusCode.success)

    def test_set_frequency_unit_Hz(self):
        freq = 500
        unit = 'Hz'
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result = lcr.set_frequency(freq, unit)

        self.assertEqual(result[1], StatusCode.success)

    def test_set_frequency_unit_kHz(self):
        freq = 500
        unit = 'kHz'
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result = lcr.set_frequency(freq, unit)

        self.assertEqual(result[1], StatusCode.success)

    def test_set_frequency_unit_MHz(self):
        freq = 1
        unit = 'MHz'
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result = lcr.set_frequency(freq, unit)

        self.assertEqual(result[1], StatusCode.success)

    def test_get_frequency(self):
        freq = 500
        unit = 'Hz'
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result_set = lcr.set_frequency(freq, unit)
        result_get = lcr.get_frequency()

        self.assertEqual(result_set[1], StatusCode.success)
        self.assertEqual(result_get, freq)

    def test_set_impedance_type_ZTD(self):
        imp_type = 'ZTD'
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result = lcr.set_impedance_type(imp_type)

        self.assertEqual(result[1], StatusCode.success)

    def test_set_impedance_type_ZTR(self):
        imp_type = 'ZTR'
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result = lcr.set_impedance_type(imp_type)

        self.assertEqual(result[1], StatusCode.success)

    def test_get_impedance(self):
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result = lcr.get_impedance()

        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 3)
        self.assertEqual(type(result[0]), float)
        self.assertEqual(type(result[1]), float)

    def test_get_impedance_delayed(self):
        delay = 2
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result = lcr.get_impedance(delay)

        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 3)
        self.assertEqual(type(result[0]), float)
        self.assertEqual(type(result[1]), float)

    def test_set_freq_and_get_impedance(self):
        freq = 500
        unit = 'Hz'
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result_set = lcr.set_frequency(freq, unit)
        result = lcr.get_impedance()

        self.assertEqual(result_set[1], StatusCode.success)
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 3)
        self.assertEqual(type(result[0]), float)
        self.assertEqual(type(result[1]), float)

    def test_set_lowest_freq_and_get_impedance(self):
        freq = 20
        unit = 'Hz'
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result_set = lcr.set_frequency(freq, unit)
        result = lcr.get_impedance()

        self.assertEqual(result_set[1], StatusCode.success)
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 3)
        self.assertEqual(type(result[0]), float)
        self.assertEqual(type(result[1]), float)

    def test_set_impedance_range(self):
        imp_range = 10
        visa_addr = get_visaaddr()
        lcr = Agilent4284A(visa_addr)
        result = lcr.set_impedance_range(imp_range)

        self.assertEqual(result[1], StatusCode.success)

if __name__ == '__main__':
    unittest.main()

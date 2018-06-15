
import visa

# class file for Precision LCR Meter
# Agilent 4284A with VISA interface

# for more info, please refer to the official document
# https://literature.cdn.keysight.com/litweb/pdf/04284-97020.pdf?id=1000002667-1:epsg:man


class Agilent4284A:
    def __init__(self, visaaddr='GPIB0::3::INSTR'):
        rm = visa.ResourceManager()
        self.inst = rm.get_instrument(visaaddr)

    def set_frequency(self, frequency, unit='Hz'):
        """Set frequency of measurement.

        Parameters
        ----------
        frequency : integer
            Frequency to be set for impedance measurement
        unit (optional): String
            unit of frequency.  select from following list
            ['Hz', 'kHz', 'MHz']
            default : 'Hz'

        Returns
        -------
        (int, pyvisa.constants.StatusCode)
            result of pyvisa write function
        """
        retval = self.inst.write("FREQ " + str(frequency) + unit)
        self.inst.write("*WAI")
        return retval

    def get_frequency(self):
        """Get frequency of measurement.

        Returns
        -------
        Float
            frequency value in Hz

        """
        return float(self.inst.query("FREQ?"))

    def set_impedance_type(self, imp_type):
        """Set impedance type

        Parameters
        ----------
        imp_type : String
            Specified impedance type. select from following list.
            'CPD' : Cp-D
            'CPQ' : Cp-Q
            'CPG' : Cp-G
            'CPRP' : Cp-Rp
            'CSD' : Cs-D
            'CSQ' : Cs-Q
            'CSG' : Cs-G
            'CSRS' : Cs-Rs
            'LPQ' : Lp-Q
            'LPD' : Lp-D
            'LPG' : Lp-G
            'LPRP' : Lp-Rp
            'LSQ' : Ls-Q
            'LSD' : Ls-D
            'LSG' : Ls-G
            'LSRS' : Ls-Rs
            'RX' : R-X
            'ZTD' : Z-theta (deg)
            'ZTR' : Z-theta (rad)
            'GB' : G-B
            'YTD' : Y-theta (deg)
            'YTR' : Y-theta (rad)

        Returns
        -------
        (int, pyvisa.constants.StatusCode)
            result of pyvisa write function

        """
        retval = self.inst.write("FUNC:IMP " + imp_type)
        self.inst.write("*WAI")
        return retval

    def set_impedance_range(self, imp_range):
        """Set impedance measurement range

        Parameters
        ----------
        imp_range : int
            range of impedance. choose from following list.
            [1, 10, 30, 100, 1000, 3000, 10000, 30000, 100000]

        Returns
        -------
        (int, pyvisa.constants.StatusCode)
            result of pyvisa write function

        """
        retval = self.inst.write("FUNC:IMP:RANG " + str(imp_range))
        self.inst.write("*WAI")
        return retval

    def trigger_immediate(self):
        """Trigger measurement immediately

        Returns
        -------
        (int, pyvisa.constants.StatusCode)
            result of pyvisa write function

        """
        retval = self.inst.write("TRIG:IMM")
        self.inst.write("*WAI")
        return retval

    def get_impedance(self, delay=None):
        self.trigger_immediate()
        raw_string = self.inst.query("FETCh:IMP?", delay).split(',')
        retval = [float(s) for s in raw_string]
        return retval

    def get_id(self):
        """Get id of the current instrument

        Returns
        -------
        String
            ID of instrument

        """
        return self.inst.query("*IDN?")

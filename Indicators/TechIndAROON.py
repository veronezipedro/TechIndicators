from TechIndicator import TechnicalIndicator
from talib import AROON
from pandas import DataFrame
from pandas import concat
__author__ = 'Pedro Henrique Veronezi e Sa'


class TechnicalIndicatorAROON(TechnicalIndicator):
    """
    Wrapper for the AROON from TA-lib
    References:
        https://github.com/mrjbq7/ta-lib
        http://www.tadoc.org/indicator/AROON.htm
    """

    def __init__(self, timeperiod=5):
        """
        Constructor with no parameters.
        Returns:
            self
        """
        super(TechnicalIndicatorAROON, self).__init__()
        self.__timeperiod = timeperiod

    def _calc_indicator(self, OHLCV_input):
        """
        Calculates the Bollinger bands technical indicator using a wrapper for the TA-lib

        Args:
            :param OHLCV_input:  the dataframe with the Open, High, Low, Close and Volume values
            :type OHLCV_input: pandas DataFrame

        Returns:
            DataFrame with scaled features with size (n_observations, n_features).
        """
        try:
            high = OHLCV_input['high'].values[:, 0]
        except IndexError:
            high = OHLCV_input['high'].values

        try:
            low = OHLCV_input['low'].values[:, 0]
        except IndexError:
            low = OHLCV_input['low'].values

        aroondown, aroonup = AROON(high, low, self.__timeperiod)

        aroondown = DataFrame(aroondown)
        aroonup = DataFrame(aroonup)

        aroondown.columns = ["aroondown"]
        aroonup.columns = ["aroonup"]

        output = concat([aroondown, aroonup], axis=1, ignore_index=True)
        return output

    def _get_max_periodNaN(self):
        """
        Getter for the number of bars to be gathered form previous periods
        Returns:
            An integer representing the number of bars to be added
        """
        # Defines the max for this application
        return self.__timeperiod

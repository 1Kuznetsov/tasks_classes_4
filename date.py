from datetime import datetime as dt


class Date:
    """
    Class representing date
    """

    months = {
        1: 'янв',
        2: 'фев',
        3: 'мар',
        4: 'апр',
        5: 'май',
        6: 'июн',
        7: 'июл',
        8: 'авг',
        9: 'сен',
        10: 'окт',
        11: 'ноя',
        12: 'дек'
    }
    start_date = dt.strptime('01.01.1970', '%d.%m.%Y')

    def __init__(self, ptr_date):
        """
        Sets all the necessary attributes for the class Date
        :param ptr_date: string of date
        """

        try:
            self.__date = dt.strptime(ptr_date, '%d.%m.%Y')

        except ValueError:
            print('ERROR')
            self.__date = None

    @property
    def date(self):
        if self.__date:
            return f'{self.__date.day} {Date.months[self.__date.month]} {self.__date.year} г.'
        return None

    @date.setter
    def date(self, value):
        try:
            self.__date = dt.strptime(value, '%d.%m.%Y')

        except ValueError:
            self.__date = None

    def to_timestamp(self):
        """
        Method returns amount of seconds since 01.01.1970
        :return: seconds since 01.01.1970
        """

        time_diff = self.__date - Date.start_date
        return int(time_diff.total_seconds())

    def __repr__(self):
        """
        Method of representing data of class Date
        :return: string of data of the class Date
        """

        if self.__date:
            return f'{self.__date.day} {Date.months[self.__date.month]} {self.__date.year} г.'
        print('ERROR')
        return str(self.__date)

    def __it__(self, other):
        """
        Method of comparison dates for < operation
        :param other: other date
        :return: Boolean result of operation
        """

        return self.__date < other.__date

    def __le__(self, other):
        """
        Method of comparison dates for <= operation
        :param other: other date
        :return: Boolean result of operation
        """

        return self.__date <= other.__date

    def __eq__(self, other):
        """
        Method of comparison dates for == operation
        :param other: other date
        :return: Boolean result of operation
        """

        return self.__date == other.__date

    def __ne__(self, other):
        """
        Method of comparison dates for != operation
        :param other: other date
        :return: Boolean result of operation
        """

        return self.__date != other.__date

    def __gt__(self, other):
        """
        Method of comparison dates for > operation
        :param other: other date
        :return: Boolean result of operation
        """

        return self.__date > other.__date

    def __ge__(self, other):
        """
        Method of comparison dates for > operation
        :param other: other date
        :return: Boolean result of operation
        """

        return self.__date >= other.__date

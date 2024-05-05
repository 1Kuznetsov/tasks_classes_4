class AirTicket:
    """
    Class representing air ticket
    """

    def __init__(self, name, _from, to, date_time, flight, seat, _class, gate):
        """
        Sets all the necessary attributes for the class AirTicket
        :param name:
        :param _from:
        :param to:
        :param date_time:
        :param flight:
        :param seat:
        :param _class:
        :param gate:
        """

        self.passenger_name = name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate

    def __repr__(self):
        """
        Method of representing data of the class AirTicket
        :return:
        """

        return '|{:<16}|{:<4}|{:<3}|{:<16}|{:<20}|{:<4}|{:<3}|{:<4}|'.format(self.passenger_name, self._from, self.to,
                                                                             self.date_time, self.flight, self.seat,
                                                                             self._class, self.gate)


class Load:
    """
    Class representing loading data from the file
    """

    data = []

    @staticmethod
    def write(filename):
        """
        Method of loading data from the file
        :param filename:
        :return:
        """

        with open(filename, 'r', encoding='utf8') as f_in:
            f_in.readline()
            for ptr in f_in:
                ptr = ptr[:-1]
                lst = ptr.split(';')
                Load.data.append(AirTicket(*lst))

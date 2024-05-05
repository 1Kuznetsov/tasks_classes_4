from datetime import datetime as dt
import locale
locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"
)


class Meeting:
    """
    Class representing Meeting
    """

    lst_meeting = []

    def __init__(self, id, date, title, employees):
        """
        Sets all the necessary attributes for the class Meeting
        :param id:
        :param date:
        :param title:
        :param employees:
        """

        self.id = id
        self.date = dt.strptime(date, '%d.%m.%Y')
        self.title = title
        self.employees = employees

    def add_person(self, person):
        """
        Method of adding new person to meeting list
        :param person:
        :return:
        """

        out = ''
        for key, val in person.items():
            if val != '':
                out += f'{key.upper()}: {val} '
        out += '\n'
        self.employees.append(out)

    def count(self):
        """
        Method of counting amount of meeting members
        :return: number of meeting members
        """

        return len(self.employees)

    @staticmethod
    def count_meeting(date):
        """
        Method of counting amount of meeting during the certain day
        :param date:
        :return: number of meetings
        """

        cnt = 0
        for elem in Meeting.lst_meeting:
            if elem.date == date.date:
                cnt += 1
        return cnt

    @staticmethod
    def total():
        """
        Method of counting total number of members of meetings
        :return:
        """

        cnt = 0
        for elem in Meeting.lst_meeting:
            cnt += len(elem.employees)
        return cnt

    def __repr__(self):
        """
        Method of representing data of class Meeting
        :return: string of data of the class Meeting
        """

        empl = ''.join(self.employees)
        date_str = self.date.strftime('%d %b %Y')

        return f'Рабочая встреча {self.id}\n' \
               f'{date_str} г. {self.title}\n' \
               f'{empl}'


class Load:
    """
    Class representing loading data from the file
    """

    @staticmethod
    def write(meet, pers, meet_pers):
        """
        Method of loading data from the file
        :param meet: txt document with info about meetings
        :param pers: txt document with info about employees
        :param meet_pers: txt document with info about members of meetings
        :return:
        """

        with open(meet, 'r', encoding='utf8') as f_meet:
            params = f_meet.readline().split(';')
            for ptr in f_meet:
                ptr = ptr.split(';')
                Meeting.lst_meeting.append(Meeting(*ptr[:-1], []))

        with open(pers, 'r', encoding='utf8') as f_pers:
            pers_dict = User.analyze_data(f_pers)

        with open(meet_pers, 'r', encoding='utf8') as f_meet_pers:
            params = f_meet_pers.readline().split(';')
            for ptr in f_meet_pers:
                ptr = ptr.split(';')
                Meeting.lst_meeting[int(ptr[0])-1].add_person(pers_dict[ptr[1]])


class Date:
    """
    Class representing date
    """

    def __init__(self, date):
        """
        Sets all the necessary attributes for the class Date
        :param date: string of data of the class Date
        """

        self.date = dt.strptime(date, '%d.%m.%Y')

    def __repr__(self):
        """
        Method of representing data of class Date
        :return:
        """

        return self.date


class User:
    """
    Class representing User
    """

    @staticmethod
    def analyze_data(f_pers):
        """
        Method of analyzing user data
        :param f_pers: file with data about employees
        :return: dictionary with staff data
        """

        pers_dict = {}
        params = f_pers.readline().split(';')

        for ptr in f_pers:
            ptr = ptr.split(';')
            pers_dict[ptr[0]] = {}
            for i in range(len(params) - 1):
                pers_dict[ptr[0]][params[i]] = ptr[i]

        return pers_dict

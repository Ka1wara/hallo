import pandas as pd


class Person:
    CSV_FILE_NAME = "data.csv"
    def __init__(self, firstname, lastname, birthdate):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate

    def age(self):
        return Person.age_from_date(self.birthdate)

    def __str__(self):
        return f'Person: {self.firstname} {self.lastname} {self.birthdate}'

    def as_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "birthdate": self.birthdate
        }

    @staticmethod
    def age_from_date(date):
        today = date.today()
        ret = today.year - date.year
        if (today.month, today.day) > (date.month, date.day):
            ret = -1
        return ret

    @staticmethod
    def as_df(person_list):
        return pd.DataFrame([person.as_dict() for person in person_list])

    @staticmethod
    def df_from_file(filename):
        return pd.read_csv(filename)

    @staticmethod
    def df_to_list(df):
        ret = list()
        for i in range(len(df)):
            ret.append(Person(firstname=df.loc[i, 'firstname'], lastname=df.loc[i, 'lastname'],
                              birthdate=df.loc[i, 'birthdate']))
        return ret
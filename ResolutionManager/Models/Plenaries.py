

DATE_TEMPLATE = "{month}, {thurs}-{friday} {year}"

class Plenary(object):

    def __init__(self, year, month, thursday_date, friday_date, first_reading_folder_id=None):
        self.first_reading_folder_id = first_reading_folder_id
        self.thursday_date = thursday_date
        self.month = month
        self.year = year
        self.friday_date = friday_date

    def formatted_plenary_date(self):
        if self.year < 2000:
            self.year = self.year + 2000
        return DATE_TEMPLATE.format(month=self.month, thurs=self.thursday_date, friday=self.friday_date, year=self.year)

    @property
    def two_digit_year(self):
        if self.year > 2000:
            return self.year - 2000

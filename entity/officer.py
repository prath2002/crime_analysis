class Officer:
    def __init__(self, officer_id=None, first_name=None, last_name=None, badge_number=None, rank=None,
                 contact_information=None, agency_id=None):
        self._officer_id = officer_id
        self._first_name = first_name
        self._last_name = last_name
        self._badge_number = badge_number
        self._rank = rank
        self._contact_information = contact_information
        self._agency_id = agency_id

    @property
    def officer_id(self):
        return self._officer_id

    @officer_id.setter
    def officer_id(self, value):
        self._officer_id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def badge_number(self):
        return self._badge_number

    @badge_number.setter
    def badge_number(self, value):
        self._badge_number = value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    @property
    def contact_information(self):
        return self._contact_information

    @contact_information.setter
    def contact_information(self, value):
        self._contact_information = value

    @property
    def agency_id(self):
        return self._agency_id

    @agency_id.setter
    def agency_id(self, value):
        self._agency_id = value

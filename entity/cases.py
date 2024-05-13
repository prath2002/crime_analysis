class Case:
    def __init__(self, case_id=None, case_description=None, case_status=None):
        self.__case_id = case_id
        self.__case_description = case_description
        self.__case_status = case_status

    @property
    def case_id(self):
        return self.__case_id

    @case_id.setter
    def case_id(self, value):
        self.__case_id = value

    @property
    def case_description(self):
        return self.__case_description

    @case_description.setter
    def case_description(self, value):
        self.__case_description = value

    @property
    def case_status(self):
        return self.__case_status

    @case_status.setter
    def case_status(self, value):
        self.__case_status = value

class IncidentType:
    def __init__(self, type_id=None, type_name=None):
        self.__type_id = type_id
        self.__type_name = type_name

    @property
    def type_id(self):
        return self.__type_id

    @type_id.setter
    def type_id(self, value):
        self.__type_id = value

    @property
    def type_name(self):
        return self.__type_name

    @type_name.setter
    def type_name(self, value):
        self.__type_name = value

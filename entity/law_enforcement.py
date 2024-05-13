class LawEnforcementAgency:
    def __init__(self, agency_id=None, agency_name=None, jurisdiction=None, contact_information=None):
        self._agency_id = agency_id
        self._agency_name = agency_name
        self._jurisdiction = jurisdiction
        self._contact_information = contact_information

    @property
    def agency_id(self):
        return self._agency_id

    @agency_id.setter
    def agency_id(self, value):
        self._agency_id = value

    @property
    def agency_name(self):
        return self._agency_name

    @agency_name.setter
    def agency_name(self, value):
        self._agency_name = value

    @property
    def jurisdiction(self):
        return self._jurisdiction

    @jurisdiction.setter
    def jurisdiction(self, value):
        self._jurisdiction = value

    @property
    def contact_information(self):
        return self._contact_information

    @contact_information.setter
    def contact_information(self, value):
        self._contact_information = value

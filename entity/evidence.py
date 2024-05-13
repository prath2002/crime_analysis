class Evidence:
    def __init__(self, evidence_id=None, description=None, location_found=None, incident_id=None):
        self._evidence_id = evidence_id
        self._description = description
        self._location_found = location_found
        self._incident_id = incident_id

    @property
    def evidence_id(self):
        return self._evidence_id

    @evidence_id.setter
    def evidence_id(self, value):
        self._evidence_id = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def location_found(self):
        return self._location_found

    @location_found.setter
    def location_found(self, value):
        self._location_found = value

    @property
    def incident_id(self):
        return self._incident_id

    @incident_id.setter
    def incident_id(self, value):
        self._incident_id = value

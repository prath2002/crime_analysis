class Incident:
    def __init__(self, incident_id=None, incident_type=None, incident_date=None, location_latitude=None,
                 location_longitude=None, description=None, status=None, victim_id=None, suspect_id=None):
        self._incident_id = incident_id
        self._incident_type = incident_type
        self._incident_date = incident_date
        self._location_latitude = location_latitude
        self._location_longitude = location_longitude
        self._description = description
        self._status = status
        self._victim_id = victim_id
        self._suspect_id = suspect_id

    @property
    def incident_id(self):
        return self._incident_id

    @incident_id.setter
    def incident_id(self, value):
        self._incident_id = value

    @property
    def incident_type(self):
        return self._incident_type

    @incident_type.setter
    def incident_type(self, value):
        self._incident_type = value

    @property
    def incident_date(self):
        return self._incident_date

    @incident_date.setter
    def incident_date(self, value):
        self._incident_date = value

    @property
    def location_latitude(self):
        return self._location_latitude

    @location_latitude.setter
    def location_latitude(self, value):
        self._location_latitude = value

    @property
    def location_longitude(self):
        return self._location_longitude

    @location_longitude.setter
    def location_longitude(self, value):
        self._location_longitude = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def victim_id(self):
        return self._victim_id

    @victim_id.setter
    def victim_id(self, value):
        self._victim_id = value

    @property
    def suspect_id(self):
        return self._suspect_id

    @suspect_id.setter
    def suspect_id(self, value):
        self._suspect_id = value

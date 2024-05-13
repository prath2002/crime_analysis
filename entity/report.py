class Report:
    def __init__(self, report_id=None, incident_id=None, reporting_officer_id=None, report_date=None,
                 report_details=None, status=None):
        self._report_id = report_id
        self._incident_id = incident_id
        self._reporting_officer_id = reporting_officer_id
        self._report_date = report_date
        self._report_details = report_details
        self._status = status

    @property
    def report_id(self):
        return self._report_id

    @report_id.setter
    def report_id(self, value):
        self._report_id = value

    @property
    def incident_id(self):
        return self._incident_id

    @incident_id.setter
    def incident_id(self, value):
        self._incident_id = value

    @property
    def reporting_officer_id(self):
        return self._reporting_officer_id

    @reporting_officer_id.setter
    def reporting_officer_id(self, value):
        self._reporting_officer_id = value

    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value

    @property
    def report_details(self):
        return self._report_details

    @report_details.setter
    def report_details(self, value):
        self._report_details = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

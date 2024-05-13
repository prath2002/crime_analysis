# exception/MyExceptions.py

class IncidentIDNotFoundException(Exception):
    """Exception raised when an invalid incident number is provided."""

    def __init__(self, message="Incident ID not found"):
        self.message = message
        super().__init__(self.message)

class VictimNotFoundException(Exception):
    """Exception raised when a victim is not found in the database."""

    def __init__(self, message="Victim not found"):
        self.message = message
        super().__init__(self.message)

class SuspectNotFoundException(Exception):
    """Exception raised when a suspect is not found in the database."""

    def __init__(self, message="Suspect not found"):
        self.message = message
        super().__init__(self.message)

class LawEnforcementAgencyNotFoundException(Exception):
    """Exception raised when a law enforcement agency is not found in the database."""

    def __init__(self, message="Law enforcement agency not found"):
        self.message = message
        super().__init__(self.message)

class OfficerNotFoundException(Exception):
    """Exception raised when an officer is not found in the database."""

    def __init__(self, message="Officer not found"):
        self.message = message
        super().__init__(self.message)

class EvidenceNotFoundException(Exception):
    """Exception raised when evidence is not found in the database."""

    def __init__(self, message="Evidence not found"):
        self.message = message
        super().__init__(self.message)

class ReportNotFoundException(Exception):
    """Exception raised when a report is not found in the database."""

    def __init__(self, message="Report not found"):
        self.message = message
        super().__init__(self.message)

class CaseNotFoundException(Exception):
    """Exception raised when a case is not found in the database."""

    def __init__(self, message="Case not found"):
        self.message = message
        super().__init__(self.message)

class IncidentTypeNotFoundException(Exception):
    """Exception raised when an incident type is not found in the database."""

    def __init__(self, message="Incident type not found"):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionError(Exception):
    """Exception raised when there is an error connecting to the database."""

    def __init__(self, message="Error connecting to the database"):
        self.message = message
        super().__init__(self.message)

class IncidentDateInvalidException(Exception):
    """Exception raised when an invalid incident date is provided."""

    def __init__(self, message="Invalid incident date"):
        self.message = message
        super().__init__(self.message)

class IncidentTypeInvalidException(Exception):
    """Exception raised when an invalid incident type is provided."""

    def __init__(self, message="Invalid incident type"):
        self.message = message
        super().__init__(self.message)

class IncidentDescriptionInvalidException(Exception):
    """Exception raised when an invalid incident description is provided."""

    def __init__(self, message="Invalid incident description"):
        self.message = message
        super().__init__(self.message)

from typing import List, Collection
from datetime import datetime
from entity.incident import Incident
from entity.cases import Case
from entity.report import Report
from entity.incident_type import IncidentType
from exception.my_exceptions import (
    IncidentIDNotFoundException,
    IncidentTypeNotFoundException,
    CaseNotFoundException,
    IncidentDateInvalidException,
    IncidentTypeInvalidException,
    IncidentDescriptionInvalidException,
    DatabaseConnectionError
)
from util.db_connection import DBConnection


class CrimeAnalysisServiceImpl:
    connection = None

    def __init__(self):
        # Initialize the database connection
        try:
            self.connection = DBConnection.get_connection()
        except Exception as e:
            raise DatabaseConnectionError(f"Error connecting to the database: {e}")

    def createIncident(self, incident: Incident) -> bool:
        try:
            # Check if the incident date is not in the future
            incident_date = datetime.strptime(incident.get_incident_date(), "%Y-%m-%d").date()
            if incident_date > datetime.now().date():
                raise IncidentDateInvalidException("Incident date cannot be a future date.")

            # Validate incident type
            if not incident.get_incident_type().isalpha():
                raise IncidentTypeInvalidException("Incident type should only contain alphabetic characters.")

            # Validate incident description
            if not incident.get_description().replace(" ", "").isalpha():
                raise IncidentDescriptionInvalidException("Incident description should only contain alphabetic characters.")

            # Continue with the rest of the code for creating the incident
            cursor = self.connection.cursor()
            query = "INSERT INTO Incident (incident_type, incident_date, location_latitude, location_longitude, description, status, victim_id, suspect_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
                incident.get_incident_type(), incident.get_incident_date(), incident.get_location_latitude(),
                incident.get_location_longitude(), incident.get_description(), incident.get_status(),
                incident.get_victim_id(), incident.get_suspect_id()))
            self.connection.commit()

            # Get the last inserted incident ID
            incident_id = cursor.lastrowid

            # Set the incident ID to the incident object
            incident.set_incident_id(incident_id)

            return True
        except (IncidentDateInvalidException, IncidentTypeInvalidException, IncidentDescriptionInvalidException) as e:
            print(f"Error creating incident: {e}")
            return False
        except Exception as e:
            print(f"Error creating incident: {e}")
            return False

    def updateIncidentStatus(self, status: str, incident_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Incident SET status = %s WHERE incident_id = %s"
            cursor.execute(query, (status, incident_id))
            if cursor.rowcount == 0:
                raise IncidentIDNotFoundException(f"Incident with ID {incident_id} not found")
            self.connection.commit()
            return True
        except IncidentIDNotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error updating incident status: {e}")
            return False

    def getIncidentsInDateRange(self, start_date: datetime, end_date: datetime) -> Collection[Incident]:
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Incident WHERE incident_date BETWEEN %s AND %s"
            cursor.execute(query, (start_date, end_date))
            incidents = []
            for row in cursor.fetchall():
                incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                incidents.append(incident)
            return incidents
        except Exception as e:
            print(f"Error getting incidents in date range: {e}")
            return []

    def searchIncidents(self, criteria: IncidentType) -> Collection[Incident]:
        cursor = self.connection.cursor()
        query = "SELECT * FROM Incident WHERE incident_type = %s"
        cursor.execute(query, (criteria.get_type_name(),))
        incidents = []
        for row in cursor.fetchall():
            incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            incidents.append(incident)
        if not incidents:
            raise IncidentTypeNotFoundException(f"Incident type '{criteria.get_type_name()}' not found")
        return incidents

    def generateIncidentReport(self, incident: Incident) -> Report:
        try:
            # Implement code to generate incident report
            # For example:
            report_details = f"Report for Incident ID: {incident.get_incident_id()}, Date: {incident.get_incident_date()}, Type: {incident.get_incident_type()}"
            report = Report(report_id=None, report_content=report_details)
            return report
        except Exception as e:
            print(f"Error generating incident report: {e}")
            return None

    def createCase(self, case_description: str, incidents: List[Incident]) -> Case:
        try:
            cursor = self.connection.cursor()

            # Insert case description into the Cases table
            query_insert_case = "INSERT INTO Cases (case_description) VALUES (%s)"
            cursor.execute(query_insert_case, (case_description,))
            case_id = cursor.lastrowid

            # Associate incidents with the case
            for incident in incidents:
                query_insert_case_incident = "INSERT INTO Case_Incident (case_id, incident_id) VALUES (%s, %s)"
                cursor.execute(query_insert_case_incident, (case_id, incident.get_incident_id()))

            self.connection.commit()
            new_case = Case(case_id, case_description, incidents)
            return new_case
        except Exception as e:
            print(f"Error creating case: {e}")
            return None

    def getCaseDetails(self, case_id: int) -> Case:
        try:
            cursor = self.connection.cursor()
            query_case_details = "SELECT * FROM Cases WHERE case_id = %s"
            cursor.execute(query_case_details, (case_id,))
            row = cursor.fetchone()
            if row:
                case_description = row[1]
                # Retrieve associated incidents
                query_incidents = "SELECT * FROM Case_Incident WHERE case_id = %s"
                cursor.execute(query_incidents, (case_id,))
                incidents = []
                for row in cursor.fetchall():
                    incident_id = row[1]
                    # Fetch incident details
                    incident = self.getIncidentById(incident_id)
                    incidents.append(incident)
                case = Case(case_id, case_description, incidents)
                return case
            else:
                raise CaseNotFoundException(f"Case with ID {case_id} not found")
        except CaseNotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error getting case details: {e}")
            return None

    def updateCaseDetails(self, case: Case) -> bool:
        try:
            cursor = self.connection.cursor()
            query_update_case = "UPDATE Cases SET case_description = %s WHERE case_id = %s"
            cursor.execute(query_update_case, (case.get_case_description(), case.get_case_id()))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating case details: {e}")
            return False

    def getAllCases(self) -> List[Case]:
        try:
            cursor = self.connection.cursor()
            query_all_cases = "SELECT * FROM Cases"
            cursor.execute(query_all_cases)
            all_cases = []
            for row in cursor.fetchall():
                case_id = row[0]
                case_description = row[1]
                # Retrieve associated incidents
                query_incidents = "SELECT * FROM Case_Incident WHERE case_id = %s"
                cursor.execute(query_incidents, (case_id,))
                incidents = []
                for row in cursor.fetchall():
                    incident_id = row[1]
                    # Fetch incident details
                    incident = self.getIncidentById(incident_id)
                    incidents.append(incident)
                case = Case(case_id, case_description, incidents)
                all_cases.append(case)
            return all_cases
        except Exception as e:
            print(f"Error getting all cases: {e}")
            return []

    def getIncidentById(self, incident_id: int) -> Incident:
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Incident WHERE incident_id = %s"
            cursor.execute(query, (incident_id,))
            row = cursor.fetchone()
            if row:
                return Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            else:
                return None
        except Exception as e:
            print(f"Error getting incident by ID: {e}")
            return None

    def deleteCase(self, case_id: int) -> bool:
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Cases WHERE case_id = %s"
            cursor.execute(query, (case_id,))
            if cursor.rowcount == 0:
                raise CaseNotFoundException(f"Case with ID {case_id} not found.")
            self.connection.commit()

            # Reset auto-increment counter after successful deletion
            self.reset_auto_increment("Cases")

            return True
        except CaseNotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error deleting case: {e}")
            return False

    def reset_auto_increment(self, table_name: str) -> None:
        """Reset the auto-increment counter for the specified table."""
        try:
            cursor = self.connection.cursor()
            query = f"ALTER TABLE {table_name} AUTO_INCREMENT = 1"
            cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print(f"Error resetting auto-increment for {table_name}: {e}")

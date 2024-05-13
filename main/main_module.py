from dao.impl_crime_analysis_service import CrimeAnalysisServiceImpl
from datetime import datetime
from entity.incident import Incident
from entity.report import Report
from entity.incident_type import IncidentType
from entity.cases import Case
from exception.my_exceptions import DatabaseConnectionError, IncidentIDNotFoundException, IncidentTypeNotFoundException,CaseNotFoundException

class MainModule:

    @staticmethod
    def get_incident_details():
        # Get input for creating an incident
        incident_type = input("Enter incident type: ")
        incident_date = input("Enter incident date (YYYY-MM-DD): ")
        location_latitude = input("Enter location latitude: ")
        location_longitude = input("Enter location longitude: ")
        description = input("Enter incident description: ")
        status = input("Enter incident status: ")
        victim_id = input("Enter victim ID: ")
        suspect_id = input("Enter suspect ID: ")
        # Create an instance of Incident with the provided details
        incident = Incident(None, incident_type, incident_date, location_latitude, location_longitude, description, status, victim_id, suspect_id)
        return incident

    @staticmethod
    def display_incidents(incidents):
        print("\nIncidents:")
        # Sort incidents by date in ascending order
        sorted_incidents = sorted(incidents, key=lambda x: x.get_incident_date())
        for incident in sorted_incidents:
            print(
                f"Incident ID: {incident.get_incident_id()}, Type: {incident.get_incident_type()}, Date: {incident.get_incident_date()}, Status: {incident.get_status()}")

    @staticmethod
    def main():
        try:
            # Create an instance of the service implementation
            crime_analysis_service = CrimeAnalysisServiceImpl()

            while True:
                # Display menu options
                print("\n" + "-" * 52)
                print("|" + " " * 20 + "Welcome to" + " " * 20 + "|")
                print("|" + " " * 6 + "'Crime Analysis and Reporting System'" + " " * 7 + "|")
                print("-" * 52)
                print("\nMenu:")
                print("1.  Add Incident")
                print("2.  View Incident Details")
                print("3.  Update Incident Status")
                print("4.  Delete Incident")
                print("5.  Search Incidents by Type")
                print("6.  Get Incidents in Date Range")
                print("7.  Generate Incident Report")
                print("8.  View Incident Report")
                print("9.  Update Incident Report Status")
                print("10. Delete Incident Report")
                print("11. Create Case")
                print("12. Get Case Details (For Specific Case ID)")
                print("13. Update Case Details")
                print("14. Get All Cases")
                print("15. Delete Case")
                print("16. Exit")

                choice = input("\nEnter your choice: ")

                if choice == '1':
                    incident = MainModule.get_incident_details()
                    if crime_analysis_service.createIncident(incident):
                        print("Incident details added successfully.")
                    else:
                        print("Failed to add incident details.")

                elif choice == '2':
                    incident_id = input("Enter incident ID: ")
                    incident = crime_analysis_service.getIncidentById(incident_id)
                    if incident:
                        MainModule.display_incidents([incident])
                    else:
                        print(f"Incident with ID {incident_id} not found")

                elif choice == '3':
                    incident_id = input("Enter incident ID to update: ")
                    new_status = input("Enter new status: ")
                    try:
                        if crime_analysis_service.updateIncidentStatus(new_status, incident_id):
                            print("Incident status updated successfully.")
                        else:
                            print(f"Incident with ID {incident_id} not found")
                    except IncidentIDNotFoundException as e:
                        print(f"Error: {e}")

                elif choice == '4':
                    incident_id = input("Enter incident ID to delete: ")
                    try:
                        crime_analysis_service.deleteIncidentById(incident_id)
                        print(f"Incident with ID {incident_id} deleted successfully.")
                    except IncidentIDNotFoundException as e:
                        print(f"Error: {e}")

                elif choice == '5':
                    incident_type = input("Enter incident type to search: ")
                    criteria = IncidentType(None, incident_type)
                    try:
                        incidents = crime_analysis_service.searchIncidents(criteria)
                        MainModule.display_incidents(incidents)
                    except IncidentTypeNotFoundException as e:
                        print(f"Error searching incidents by type: {e}")

                elif choice == '6':
                    start_date = input("Enter start date (YYYY-MM-DD): ")
                    end_date = input("Enter end date (YYYY-MM-DD): ")
                    try:
                        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                        incidents = crime_analysis_service.getIncidentsInDateRange(start_date, end_date)
                        MainModule.display_incidents(incidents)
                    except ValueError as e:
                        print(f"Error: {e}")

                elif choice == '7':
                    incident_id = input("Enter incident ID to generate report: ")
                    reporting_officer_id = input("Enter reporting officer ID: ")
                    report_date = input("Enter report date (YYYY-MM-DD): ")
                    status = input("Enter report status: ")
                    try:
                        report_date = datetime.strptime(report_date, "%Y-%m-%d").date()
                        if report_date > datetime.now().date():
                            raise ValueError("Report date cannot be in the future.")
                        incident = crime_analysis_service.getIncidentById(incident_id)
                        if incident:
                            report = crime_analysis_service.generateIncidentReport(incident, reporting_officer_id, report_date, status)
                            if report:
                                print("Incident report generated successfully.")
                            else:
                                print("Failed to generate incident report.")
                        else:
                            print("Incident not found.")
                    except ValueError as e:
                        print(f"Error: {e}")

                elif choice == '8':
                    incident_id = input("Enter incident ID to view report: ")
                    try:
                        report = crime_analysis_service.getIncidentReport(incident_id)
                        if report:
                            print("Incident Report:")
                            print(f"Report ID: {report.get_report_id()}")
                            print(f"Incident ID: {report.get_incident_id()}")
                            print(f"Reporting Officer ID: {report.get_reporting_officer_id()}")
                            print(f"Report Date: {report.get_report_date()}")
                            print(f"Report Details: {report.get_report_details()}")
                            print(f"Status: {report.get_status()}")
                        else:
                            print(f"Incident report for ID {incident_id} not found.")
                    except IncidentIDNotFoundException as e:
                        print(f"Error: {e}")

                elif choice == '9':
                    report_id = input("Enter report ID to update status: ")
                    new_status = input("Enter new report status: ")
                    try:
                        if crime_analysis_service.updateIncidentReportStatus(report_id, new_status):
                            print("Incident report status updated successfully.")
                        else:
                            print(f"Error: Incident report with ID {report_id} not found.")
                    except IncidentIDNotFoundException as e:
                        print(f"Error: {e}")

                elif choice == '10':
                    report_id = input("Enter report ID to delete: ")
                    try:
                        if crime_analysis_service.deleteIncidentReport(report_id):
                            print(f"Incident report with ID {report_id} deleted successfully.")
                        else:
                            print(f"Incident report with ID {report_id} not found.")
                    except IncidentIDNotFoundException as e:
                        print(f"Error: {e}")

                elif choice == '11':
                    case_description = input("Enter case description: ")
                    case_status = input("Enter case status: ")
                    new_case = crime_analysis_service.createCase(case_description, case_status)
                    if new_case:
                        print("Case created successfully.")

                elif choice == '12':
                    case_id = input("Enter case ID to get details: ")
                    case_details = crime_analysis_service.getCaseDetails(case_id)
                    if case_details:
                        print(f"Case ID: {case_details.get_case_id()}")
                        print(f"Case Description: {case_details.get_case_description()}")
                        print(f"Case Status: {case_details.get_case_status()}")
                    else:
                        print("Case not found.")

                elif choice == '13':
                    case_id = input("Enter case ID to update: ")
                    new_description = input("Enter new case description: ")
                    try:
                        if crime_analysis_service.updateCaseDescription(case_id, new_description):
                            print("Case description updated successfully.")
                        else:
                            print(f"Case with ID {case_id} not found.")
                    except IncidentIDNotFoundException as e:
                        print(f"Error: {e}")

                elif choice == '14':
                    all_cases = crime_analysis_service.getAllCases()
                    print("\nAll Cases:")
                    for case in all_cases:
                        print(
                            f"Case ID: {case.get_case_id()}\nCase Description: {case.get_case_description()}\nCase Status: {case.get_case_status()}\n")

                elif choice == '15':
                    case_id = input("Enter case ID to delete: ")
                    try:
                        if crime_analysis_service.deleteCase(case_id):
                            print(f"Case with ID {case_id} deleted successfully.")
                        else:
                            print(f"Case with ID {case_id} not found.")
                    except CaseNotFoundException as e:
                        print(f"Error: {e}")

                elif choice == '16':
                    print("Exiting program.")
                    break

                else:
                    print("Invalid choice. Please select a valid option.")

        except DatabaseConnectionError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    MainModule.main()

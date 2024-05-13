Crime Analysis and Reporting System (C.A.R.S.)

C.A.R.S. is a comprehensive application designed to assist law enforcement agencies in managing crime data effectively. It provides functionalities for creating incidents, updating incident status, generating reports, managing cases, and more.

Directory Structure:
--------------------
.
├── entity
│   ├── __init__.py
│   ├── cases.py
│   ├── incident.py
│   ├── incident_type.py
│   ├── law_enforcement.py
│   ├── officer.py
│   ├── report.py
│   ├── suspect.py
│   └── victim.py
├── dao
│   ├── __init__.py
│   ├── crime_analysis_service.py
│   └── impl_crime_analysis_service.py
├── exception
│   ├── __init__.py
│   └── my_exceptions.py
├── util
│   ├── __init__.py
│   ├── db_connection.py
│   └── db_property_util.py
└── main
    ├── __init__.py
    └── main_module.py

Key Functionalities:
---------------------
- Schema Design: The database schema includes entities such as Incidents, Victims, Suspects, Law Enforcement Agencies, Officers, Evidence, and Reports.
- Service Provider Interface: The ICrimeAnalysisService interface provides methods for creating incidents, updating status, generating reports, managing cases, etc.
- Database Interaction: The DBConnection class establishes a connection to the SQL database using properties read from a property file.
- Service Implementation: The CrimeAnalysisService class implements the methods defined in the ICrimeAnalysisService interface, interacting with the database to perform CRUD operations.
- Exception Handling: Custom exceptions such as DatabaseConnectionError, IncidentIDNotFoundException, etc., are defined and handled throughout the application.
- Main Module: The MainModule class contains the main method and implements a menu-driven interface to interact with the functionalities provided by the service.

Getting Started:
----------------
1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Set up the database by executing the SQL scripts provided in the sql directory.
5. Update the database connection details in the config.properties file.
6. Run the MainModule.py file to start the application.

Contributors:
-------------
Pratham Agarwal

Feel free to customize the README file according to your project's specific details and requirements.

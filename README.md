# Simple-Candidature-Registry-System
This is an API REST to manage new candidates aiming joing certain tech enterprise.

## Manual:
1) Setup an enviroment using requeriments.txt.
2) On that enviroment, run server in terminal with command "python manage.py runserver 8000".
3) Open index.html .
4) From there we can see options: Manage candidates | Manage tech experience | Manage technologies
5) First option is a CRUD for candidates.
6) Second is a CRUD for Technolgy-Candidate relationship.
7) Third is a CRUD for technolgies, in case you want to add more or whatever you want.

8) Report:
For report, just write desired technology, and a new page will show a report of candidates using that technology descending by 
experience years.
## Endpoints:
1- http://127.0.0.1:8000/candidates/ --> List and create candidates.  
2- http://127.0.0.1:8000/candidates/candidate_id --> Retrieve a candidate to update or delete.  
3- http://127.0.0.1:8000/candidatetech/ --> Form for assigns technologies to candidates and experience years.  
4- http://127.0.0.1:8000/candidatetech/candidatetech_id --> Retrieve a candidatetech to update or delete.   
5- http://127.0.0.1:8000/report?tech=tech_name&Form=Submit --> List a report for the tech_name technology.

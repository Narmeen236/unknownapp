# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
```mermaid
graph LR
    %% Actors
    Student((Student)) 
    Admin((Admin)) 

    %% System Boundary
    subgraph System [Course Enrollment System]
        direction TB
        UC1(View Course Catalog)
        UC2(Register for a Course)
        UC3(Drop a Course)
        UC4(View Schedule)
        UC5(View Billing Summary)
        UC6(Manage Student Profile)
        UC7(Manage Course Data)
        UC8(View Class Roster)
    end

    %% Student Connections
    Student --- UC1
    Student --- UC2
    Student --- UC3
    Student --- UC4
    Student --- UC5
    Student --- UC6

    %% Admin Connections
    Admin --- UC1
    Admin --- UC7
    Admin --- UC8
    Admin --- UC5
```  

### Flowchart of the main workflow
```mermaid
flowchart TD
    Start([Start]) --> LoadData[Load Data from JSON]
    LoadData --> MainMenu{Login Menu}

    %% Student Path
    MainMenu -- "1. Student" --> StudentID[Input Student ID]
    StudentID --> IDType{Is 'new'?}
    IDType -- "Yes" --> CreateUser[Create Profile]
    IDType -- "No" --> VerifyID{ID Exists?}
    
    VerifyID -- "No" --> MainMenu
    VerifyID -- "Yes" --> StudentMenu[Student Dashboard]
    CreateUser --> StudentMenu
    
    StudentMenu -- "Logout" --> SaveBack[Save Data]

    %% Admin Path
    MainMenu -- "2. Admin" --> AdminPass[Input Password]
    AdminPass --> Auth{Success?}
    Auth -- "Yes" --> AdminMenu[Admin Dashboard]
    Auth -- "No" --> MainMenu
    
    AdminMenu -- "Logout" --> SaveBack
    SaveBack --> MainMenu

    %% Exit Path
    MainMenu -- "3. Exit" --> SaveExit[Final Save]
    SaveExit --> End([End Program])
```  
### Prompts

The following prompts were used with AI assistance:
 
**Prompt 1 — Use case diagram:**
> "Based on this Java Course Enrollment System, generate a Mermaid use case diagram showing all actors (Student and Admin) and their use cases, with proper styling."
 
**Prompt 2 — Mermaid flowchart:**
> "Create a Mermaid flowchart showing the user's flow through the main menu of this Course Enrollment System, including the login menu, student menu, and admin menu.
 
## Technical Implementation Details:
* **Target Use Case:** Course Registration & Validation Logic
* **System Architecture:** Implemented using a Class-based approach to maintain Object-Oriented principles from the original source.
* **Logic Constraints:** * **Capacity Guard:** Prevents enrollment if `enrolled >= capacity`.
    * **Prerequisite Filter:** Scans student history to ensure required course codes are present.
    * **State Management:** Uses local dictionaries to simulate the system's database.

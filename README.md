# Hilmar-Leak-Detection
Use Case 1:
================
Cheese Quality Inspector: 
Entry Conditions: Cheese is being produced, Cheese curd detection system has been activated
Exit Conditions: Turns off system via button

Basic flow:
Application startup: The inspector turns on the cheese curd detection application.
Image processing begins: The system starts processing images of cheese seals.
Cheese curd detected: The system identifies a cheese curd within a seal.
Notification triggered: A notification is sent to a front-end window, alerting the inspector.
Inspector investigates: The inspector investigates the detected cheese curd.
Defect identified: If the cheese curd is confirmed as a defect, the inspector takes appropriate action (e.g., reject the cheese, adjust production parameters).


Alternative flows:
Incorrect Results: Inspector dismisses the result.
No Defect found: Inspector continues waiting for an alert.


# attendanc_managing-system# Attendance Management System

This is a Django-based web application for managing attendance in an organization.

## Features

- Authentication & Authorization:
  - Implement roles: Manager and Staff.
  - Only authenticated managers can create/edit/view the roster.
  - Only authenticated staff can mark their attendance.
- Roster Management:
  - Managers can add new staff members to the roster.
  - Managers can set working days and shifts for each staff member.
  - Managers can view the complete roster.
  - Managers can edit the details of any staff member in the roster.
- Attendance Management:
  - Staff members can view their assigned shifts.
  - Staff members can mark their attendance by capturing an image using the webcam.
  - The system stores the attendance data, timestamp, and the captured image.

## Installation

1. Clone the repository:
   ```bash
   https://github.com/shaukat-123/attendanc_managing-system.git
   
2. Navigate to the project directory:
   cd attendance-management-system
3. Install dependencies:
  pip install -r requirements.txt


Usage

    To create a new user (staff or manager), make a POST request to /api/users/.
    To manage staff (list, create, retrieve, update, delete), use the /api/staff/ endpoint.
    To manage attendance (list, create, retrieve, delete), use the /api/attendance/ endpoint.
    To mark attendance by capturing an image, make a POST request to /api/mark-attendance/.

# TagCare Automation Testing Project

# Project Overview
This project contains API and UI automation tests for the TagCare application.
The objective is to validate application functionality, API responses, data consistency, authentication, pagination, and security.

# Tools and Technologies
- Python
- Pytest
- Selenium WebDriver
- Requests
- API Testing
- Git and GitHub


# API Testing
- Valid and invalid login
- Logout and token validation
- Device listing and pagination
- Device status filtering
- Device access authorization
- Device rename validation
- Ticket creation and validation
- Ticket idempotency
- Ticket update and deletion

# UI Testing
- Login page validation
- Successful and unsuccessful login
- Dashboard device counts
- Device listing
- Low-battery badges
- Device pagination
- Device status filtering
- Device rename
- Logout

## How to Execute Tests

1. Activate virtual environment
> .venv\Scripts\activate

2. Run all tests
> pytest -v -s

3. Run API tests
> pytest -v -s tests/test_devices_api.py

4. Run UI tests
> pytest -v -s tests/test_login_ui.py

5. Run authentication tests
> pytest -v -s tests/test_auth.py


# Conclusion
API and UI automation testing was performed to identify functional, validation, pagination, data consistency, and security issues. The identified defects were documented with their reproduction steps and corresponding automated test cases.
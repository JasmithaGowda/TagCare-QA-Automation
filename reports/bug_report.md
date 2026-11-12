BUG REPORT

*******************************************************************************
# BUG_001 : Duplicate devices in Pagination

defect_id: BUG_001
title:Duplicate devices in Pagination
expected_result: each device should appear only once accross all pages.no duplicate recors should be displayed
actual_result: Device DEV_1010 appears more than once across pages
severity : High (each page must contain 10 devices and no duplicate devices)

steps:
1. log in to the tagcare application.
2. naviagte to the device list
3. open the first page and note the displayed device IDS
4. Navigate to next page
5. compare devices ids on the pages


****************************************************************************
# BUG_002: Dashboard low battery count mismatch

defect_id: BUG_002
title:Dashboard low battery count mismatch
expected_result: The dashboard should display 4 low-battery devices
actual_result: The API returns 4 low-battery devices, but the dashboard displays only 2.
severity : Medium (The low-battery device count displayed on the dashboard does not match the count returned by the API.)

Steps:
1. Log in to the TagCare application.
2. Navigate to the dashboard.
3. Retrieve the low-battery device count from the API.
4. Compare the API count with the dashboard count.


****************************************************************************
# BUG_003: Missing Low-Battery Badges

defect_id: BUG_003
title: missing low-battery badges
expected_result: Low-battery badges should be displayed for all devices that meet the low-battery condition.
actual_result: low battery badges missing even the batter range is below 20%
severity : Medium (Low-battery badges are missing for certain devices that are expected to be identified as low-battery devices.

Steps:
1. Log in to the TagCare application.
2. Navigate to the device list.
3. Identify devices with low battery status.
4. Verify whether the corresponding UI badges are displayed.


****************************************************************************
# BUG-004: Device Rename Not Displayed Correctly

Defect_id : BUG_004
Title: Device Rename Not Displayed Correctly
expected result: The updated device name should be displayed even without refresh.
Actual result : The UI displays the device name after refresh or next action.
Severity : Medium

Steps to Reproduce:
1. Log in to the TagCare application.
2. Navigate to the device list.
3. Select a device and perform the rename operation.
4. Enter the new name Valid Device.
5. Verify the updated device name in the UI.


****************************************************************************
# BUG-005: Dashboard device count mismatch

Defect_id : BUG_005
Title: Dashboard device count mismatch
expected result: Dashboard device count and table devices should matched.
Actual result : Dashboard device counts are more than expected
Severity : Medium

Steps to Reproduce:
1. Log in to the TagCare application.
2. Navigate to the device list.
3. Retrieve the device count from the API.
4. Compare the API count with the dashboard count.


****************************************************************************
# BUG-006: Search filter should be case-sensitive

Defect_id : BUG_006
Title: Search filter should be case-sensitive
expected result: Search filter should accept only valid inputs.
Actual result : Search filter is accepting all type of data
Severity : Medium

Steps to Reproduce:
1. Log in to the TagCare application.
2. Navigate to the device list.
3. search for device


****************************************************************************
# BUG-007: Duplicate device is accepted with a success message

Defect_id : BUG_007
Title: Application displays "Device added" message when attempting to add a duplicate device.
Expected Result: Application should prevent duplicate device creation and display an appropriate validation message. API should return a suitable error response.
Actual Result: Application displays "Device added" even though the duplicate device is not added to the list. No API error message is displayed.
Severity : High

Steps to Reproduce:
1. Navigate to the Devices page.
2. Add a device with a unique device ID.
3. Try adding another device using the same device ID.
4. Observe the success message and device list.


****************************************************************************
# BUG-008: Incorrect alerts displayed under Open Alerts filter

Defect_id : BUG_008
Title: Open Alerts filter displays acknowledged alerts.
expected result: Only open alerts status should be displayed with an open alert button.
Actual result : Acknowledged and oepn alerts are also displayed under Open Alerts, showing an incorrect alert status and action.
Severity : Medium

Steps to Reproduce:
1.Navigate to the Alerts page.
2.Click on Open Alerts.
3.Observe the displayed alerts.


****************************************************************************
# BUG-009: Alert count does not update after acknowledging an alert

Defect_id : BUG_009
Title: Alert count is not updated after acknowledging an alert.
expected result: Alert count should decrease immediately after successfully acknowledging an alert.
Actual result :Alert count remains unchanged even after the alert is successfully acknowledged.
Severity :  High

Steps to Reproduce:
1. Navigate to the Alerts page.
2. Note the current alert count.
3. Select an open alert.
4. Click the Acknowledge button.
5. Observe the alert count.




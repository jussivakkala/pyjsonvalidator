*** Settings ***
Library     test_validations.py
Variables   test_cases.py


*** Test Cases ***
Get Test Data
    Get Some Test Data


*** Keywords ***
Get Some Test Data
    @{del_fields}=  Create List  routes  points
    Set Test Variable  &{modifications}     change_to=_ROBOT_entry_  del_keys=${del_fields}
    FOR  ${testcase}  IN  @{regression_tests}
        Log to Console  \n************************
        ${test_set}=  Json Validation  ${testcase}  ${modifications}
        Log  ${test_set}  repr=yes  console=yes
    END
    Log to Console  \n********* Data is validated O.K with schema *************



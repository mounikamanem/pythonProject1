import requests
import unittest
import json


class TestGetEmployee(unittest.TestCase):
    def test_validStatus(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
        }
        url = "https://dummy.restapiexample.com/api/v1/employees"

        resp = requests.get(url, headers=headers)
        code = resp.status_code
        self.assertEqual(code, 200, "test to validation of http success status {code}")

    def test_validStatusMessage(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
        }
        url = "https://dummy.restapiexample.com/api/v1/employees"

        resp = requests.get(url, headers=headers)
        resp_data = json.loads(resp.text)
        statusmessage = resp_data.get("status")

        self.assertEqual(statusmessage,"success","test to validate status message{statusmessage}")

    def test_validFinalMessage(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
        }
        url = "https://dummy.restapiexample.com/api/v1/employees"

        resp = requests.get(url, headers=headers)
        resp_data = json.loads(resp.text)
        finalmessage = resp_data.get("message")
        expectedmessage = "Successfully! All records has been fetched."

        self.assertEqual(finalmessage, expectedmessage, "test to validate f_msg{finalmessage}")

    def test_validEmployeeName(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
        }
        url = "https://dummy.restapiexample.com/api/v1/employee/1"

        resp = requests.get(url, headers=headers)
        resp_data = json.loads(resp.text)
        employeeobject = resp_data.get("data")
        employeename = employeeobject["employee_name"]
        expectedname = "Tiger Nixon"
        print(employeename)

        self.assertEqual(employeename, expectedname, "test to validate emp_name{employeename}")

    def test_validNameCheck(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
        }
        url = "https://dummy.restapiexample.com/api/v1/employee/1"

        resp = requests.get(url, headers=headers)
        resp_data = json.loads(resp.text)
        employeeobject = resp_data.get("data")
        employeename = employeeobject["employee_name"]
        expectedname = "Satya Prakash"
        print(employeename)

        self.assertNotEqual(employeename, expectedname, "test to validate emp_name{employeename}")


if __name__ == '__main__':
    unittest.main()

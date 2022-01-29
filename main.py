import unittest
import requests
import random
reg_url = "https://api.frs1.ott.kaltura.com/api_v3/service/ottuser/action/register"
log_url = "https://api.frs1.ott.kaltura.com/api_v3/service/ottuser/action/login"
reg_data = {
"apiVersion": "6.0.0",
"partnerId": 3197,
"user": {
  "objectType": "KalturaOTTUser",
  "username": "QATest_Aleex79",
  "firstName": "ott_user_lWkiwzTJJGYI",
  "lastName": "1585130417330",
  "email": "QATest_1585130417313@mailinator.com",
  "address": "ott_user_lWkiwzTJJGYI fake address",
  "city": "ott_user_lWkiwzTJJGYI fake city",
  "countryId": 5,
  "externalId": "316400413044979"
        },
"password": "password_SlLVWDLl"
}
log_data = {
"apiVersion": "6.0.0",
"partnerId": 3197,
"username": "QATest_Alex_1",
"password": "password_SlLVWDLl",
"extraParams": {}
}


def user_randomizer():
    # Randomization to workaround existing user failure
    reg_data['user']['externalId'] = str(random.randrange(3164004130446, 4164004130446, 1))
    reg_data['user']['username'] = 'QATest_Alex12345'.join(random.sample('QATest_Alex12345343', k=2))
    return


class APITestsRegLog(unittest.TestCase):
    # For each of the following API’s please print the request and response (body and headers)
    # Call for the following API requests using JSON (HTTP request with any HTTP client library)
    user_randomizer()

    def test_print_response_reg(self):
        # API request/response body and headers
        resp = requests.post(reg_url, json=reg_data)
        print(f'Response body#1: {resp.json()}')
        print(f'Request body#1: {reg_data}')
        print(f'Response headers#1: {resp.headers}')
        user_randomizer()

    def test_reg_header(self):
        # Assertion of existence of any response header (pick one)
        resp = requests.post(reg_url, json=reg_data)
        assert resp.headers['Transfer-Encoding'] == 'chunked', 'wrong encoding'
        user_randomizer()

    def test_reg_id_type(self):
        # Assertion if “Id” field exist and if it is of type string
        resp = requests.post(reg_url, json=reg_data)
        json_response = resp.json()
        assert json_response['result']['id'] is not None, "id item not exists"
        assert type(json_response['result']['id']) == str, 'wrong id type'
        user_randomizer()

    def test_reg_countryId(self):
        # Assertion if “countryId” field exist and if it is of type integer
        resp = requests.post(reg_url, json=reg_data)
        json_response = resp.json()
        assert json_response['result']['countryId'] is not None, "icountryId item not exists"
        assert type(json_response['result']['countryId']) == int, 'wrong countryId type'

    # Call for additional API request for login Please use the following parameters :
    # Username = username from the previous register request Password = password from the previous register request
    def test_resp_print_log(self):
        # API request/response body and headers
        resp2 = requests.post(log_url, json=log_data)
        print(f'Response body#2: {resp2.json()}')
        print(f'Request body#2: {log_data}')
        print(f'Response headers#2: {resp2.headers}')

    def test_last_log(self):
        # Assertion if “lastLoginDate” exist and present it as valid Date value (any format)
        resp2 = requests.post(log_url, json=log_data)
        json_response2 = resp2.json()
        print(f"Last Login: {json_response2['result']['user']['lastLoginDate']}")
        assert json_response2['result']['user']['lastLoginDate'] is not None, "lastLogin item not exists"
        assert type(json_response2['result']['user']['lastLoginDate']) == int, "wrong type" # TODO: Validate Date format.

    # Call for ottuser/action/register API again with the same parameters
    def test_reg_with_log(self):
        # print the following in the output console :
        # - API request/response body and headers
        # - Catch the error and print it
        resp3 = requests.post(reg_url, json=log_data)
        print(f'Response body#3: {resp3.json()}')
        print(f'Request body#3: {log_data}')
        print(f'Response headers#3: {resp3.headers}')
        for item in resp3.json()["result"]:
            if item == "error":
                print(f"Found error: {resp3.json()['result']['error']['message']}")


if __name__ == "__main__":
    unittest.main()


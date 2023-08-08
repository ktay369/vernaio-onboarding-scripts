import requests
import json


def make_post_request(url, data, token):
    try:
        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.post(url, json=data, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 201:
            print("POST request successful:")
            print("Response Content:", response.text)
        # elif response.status_code == 401:
        #     print("POST request successful:")
        #     print("Response Content:", response.text)
        else:
            print("POST request failed with status code:", response.status_code)
            print("Response Content:", response.text)
            if response.status_code == 401:
                raise Exception("Error: Check bearer token.")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


# returns a list of request jsons
def create_request_json():
    metadata_file_path = '../input/metadata.json'
    mapping_file_path = 'mapping.json'

    new_entries = []

    with open(metadata_file_path, 'r') as metadata_file:
        metadata = json.load(metadata_file)

    with open(mapping_file_path, 'r') as mapping_file:
        mapping = json.load(mapping_file)

    # signalJson0['dataType'] = { _type: fieldValue };

    for entry in metadata["signals"]:
        user_id = entry["id"]
        uuid = mapping.get(user_id)
        new_entry = {
            'id': uuid,
            'title': entry.get("name"),
            'description': entry.get("description", ""),
            # 'dataType': entry.get("dataType"),
            # 'dataType': {'_type': entry.get("dataType")},
            'dataType': {'_type': entry.get("dataType").capitalize()},
            'unitName': entry.get("unitName", ""),
            'unitSymbol': entry.get("unitSymbol", ""),
            'categoryRef': '3fa85f64-5717-4562-b3fc-2c963f66afa6'
        }
        new_entries.append(new_entry)
    return new_entries


def main():
    # account = input("Enter your account number: ")
    bearer_token = input("Enter your bearer token: ")
    # env = input("Enter your environment: ")

    account = 4930
    # bearer_token = (
    #     'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVSU3V5bXZ4T3o3Vm1ieElUbV83QyJ9.eyJvcmciOiIxOTY3NTIxNi1mZmJhLTR'
    #     'hYzItOWFhZC1kMzI3NjZkN2RjZWYiLCJpc3MiOiJodHRwczovL2xvZ2luLmV1MS52ZXJuYWlvLWRlbW8uY2xvdWQvIiwic3ViIjoiYXV0aDB8N'
    #     'jRiNTU3Mzg2YTk4OWI1MTA2MzBiYzc1IiwiYXVkIjpbImh0dHBzOi8vYXBpLmV1MS52ZXJuYWlvLWRlbW8uY2xvdWQvIiwiaHR0cHM6Ly92ZX'
    #     'JuYWlvLXZjLWRlbW8tZXUxLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTE0NDA2MjIsImV4cCI6MTY5MTQ0NDIyMiwiYXpwIjoi'
    #     'ZXBNQ09mbHFVeHJ2T2E1TW1Ia2RZSjgwckFsaGY4bFAiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwib3JnX2lkIjoib3JnX0s2Wk'
    #     'FrQzZXd2lQTzl6ajUiLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiJdfQ.VFZGVDJCAV7f2pAPcpWgmakoPluxO7hrE7FT_9F2-mzXRzIXpvUtesv5sMiquuPLQJqzfD-LK70Qmr0WaLYQwIZBmko52kWWQJwQDOogO_USS58Av_SAnhBrzCMaZrp9aeX4MoY1U2M9NSEY42R_yCmDZN-nKnAcgJnu33kLgGZU_wZys4vlaypEz7Q4QG-C3Yoaefsu74eaX4fUKaliP_J5_G0hv5tNO46ANd6Vn_4hcjiMO3ZRNbnqgcXN9n9JG3HaiBIfolnY06CIxI250utJQ9kPHewOaAU53zc2U_W66XWQDpcshKcqMHFBOwWqjd8NM8Htu_ndpMY5HbQung'
    # )
    env = 'demo'

    # bearer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVSU3V5bXZ4T3o3Vm1ieElUbV83QyJ9.eyJvcmciOiIxOTY3NTIxNi1mZmJhLTRhYzItOWFhZC1kMzI3NjZkN2RjZWYiLCJpc3MiOiJodHRwczovL2xvZ2luLmV1MS52ZXJuYWlvLWRlbW8uY2xvdWQvIiwic3ViIjoiYXV0aDB8NjRiNTU3Mzg2YTk4OWI1MTA2MzBiYzc1IiwiYXVkIjpbImh0dHBzOi8vYXBpLmV1MS52ZXJuYWlvLWRlbW8uY2xvdWQvIiwiaHR0cHM6Ly92ZXJuYWlvLXZjLWRlbW8tZXUxLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTE0MzY4MzEsImV4cCI6MTY5MTQ0MDQzMSwiYXpwIjoiZXBNQ09mbHFVeHJ2T2E1TW1Ia2RZSjgwckFsaGY4bFAiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwib3JnX2lkIjoib3JnX0s2WkFrQzZXd2lQTzl6ajUiLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiJdfQ.QyIT8vPkNEPWKc6Mmr3azVrgIstgSbrqckkWE6y5Jev_Oo8iETDFYoojzMXwwkALtPK-YuMpDfxGiEhcSj8CjtQRx7X7u345Z_8izeX12kmKjiHGBfVIPS0nktzVXE8Z2EwHQ3_7Pp8BuvMhteXkYdJ2W5PbqGoxYXqL8_fAhuiFrvq9dyTQIYq4T75-hUjnoVB0jq80uhMTadSW5jnJBSIOkRvSiWrYP42Hw_1oDWNwDqBv5OgQAD53sos3nim66FBFuqho9p1thr1V-pMn22FXKVJPrbhcN1F33yey8-m3kwrio1J42tL1mk78uRnRwQwdcF-uRtS9-ohqz_tlhQ'

    url = f"https://iiot-signal-metadata-service-v1.eu1.vernaio-{env}.cloud/accounts/{account}/signals"

    # `https://${domain}-service-v1.eu1.vernaio-${env}.cloud/accounts/${account}/` + urlPath

    json_list = create_request_json()

    for entry in json_list:
        make_post_request(url, entry, bearer_token)

    # make_post_request(url, data, bearer_token)


if __name__ == "__main__":
    main()

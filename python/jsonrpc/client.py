import requests
import json


def main():
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}
    payload = {
        "method": "omg",
        "params": {"foo": "json", "bar": "1111111111"},
        "jsonrpc": "2.0",
        "id": 3,
    }
    requests.post(url, data=json.dumps(payload), headers=headers).json()


if __name__ == "__main__":
    main()

import requests
from copy import copy


token = "4b31cf089ca8a9508f6021ca8edc52d62a620ed378107e15c8110655622582e126cdef65af04002d40c5d"


def request(request_type, method, parameters):
    print(request_type, method, parameters)

    parameters = copy(parameters)
    parameters["access_token"] = token
    parameters["v"] = "5.87"

    assert request_type in ["GET", "POST"]
    request_command = requests.get if request_type == "GET" else requests.post
    r = request_command(url="https://api.vk.com/method/" + method, params=parameters)
    data = r.json()
    print(data)


def main():
    request("GET", "users.get", {"user_ids": "id213033618"})


if __name__ == "__main__":
    main()


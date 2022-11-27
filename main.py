# This is a sample Python script.
import json

import requests
from authentication import auth_headers
from dictionaries import engines

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(auth_headers)# Press Ctrl+F8 to toggle the breakpoint.
    r = requests.get(url="http://iss.moex.com/iss/engines.json", headers=auth_headers)
    r2 = requests.get(url="http://iss.moex.com/iss/engines/stock/markets.json", headers=auth_headers)
    r3 = requests.get(url="http://iss.moex.com/iss/engines/stock/markets/bonds/trades/colums.json", headers=auth_headers)
    r4 = requests.get(url="http://iss.moex.com/iss/engines/stock/markets/bonds.json",
                      headers=auth_headers)
    r5 = requests.get(url="http://iss.moex.com/iss/securities.json", headers=auth_headers)
    # print(r.content.decode())
    # print(r2.content.decode())
    r3 = requests.get(url="https://iss.moex.com/iss/history/engines/stock/markets/bonds/boards.json",
                      headers=auth_headers)
    result = (r.content.decode())
    # print(type(result))
    # print(result)
    # print(r4.content.decode())
    # print(r5.content.decode())

    for engine in engines:
        request = requests.get(
            url=f"http://iss.moex.com/iss/engines/{engine}/markets.json"
        )
        print(engine)
        print(request.content.decode())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

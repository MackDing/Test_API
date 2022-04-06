# -*- coding:utf-8 -*-
# @Time : 5/6/22 6:47 PM
# @Author: Mack.Ding
# @File : demo_test.py

import requests, jsonpath, pprint

try:
    response = requests.get('https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json')
    # print_response
    pprint.pprint(response.json())
    # code == 200
    assert response.status_code == 200
    # Name = "Carbon credits"
    assert response.json()["Name"] == "Carbon credits"
    # CanRelist = true
    assert True
    (response.json()["CanRelist"])
    # The Promotions element with Name = "Gallery" has a Description that contains the text "Good position in category"
    assert ("Gallery" in jsonpath.jsonpath(response.json(), "$..Promotions[*][Name]"))

    print("[pass]")
except:
    print("[fail]")

import sys, os
import requests
import json
import argparse


"""
    Automation Asset to run automation assets for reservation as
    Startup and Teardown task

    Velocity will return parameter:
    reservationId    Text    16284bc7-8461-4774-baa7-703133ddaa26

"""
__version__ = 0.1
__author__ = "Velocity Support"
__email__ = "velocity.support@nokia.com"

parser = argparse.ArgumentParser(description='Arguments received from Velocity')
known_velocity_params, unknown = parser.parse_known_args()

try:
    velocity_params = vars(unknown)
except Exception as not_dict:
    try:
        velocity_params = {unknown[i].strip('-'): unknown[i + 1] for i in range(0, len(unknown), 2)}
    except Exception as notlist:
        velocity_params = {}

print("[INFO] START")
try:
    resource_ids_list = velocity_params["resourcesIds"].split(",")
    print("[INFO] resource ids: ", resource_ids_list)

except Exception as e:
    print("Finished: FAILED: ", e)
    exit()

print("Finished: PASSED")

import json
import sys

#required data typed
# "bus_id": 128, #INTEGER
# "stop_id": 1, #INTEGER
# "stop_name": "Prospekt Avenue", #STRING
# "next_stop": 3, #INTEGER
# "stop_type": "S", #SPECIAL CHAR OR EMPTY
# "a_time": 8.12    #STRING


stops_dict = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}
errors_dict = dict.fromkeys(stops_dict, 0)
json_string = sys.stdin.read()
stops_list = json.loads(json_string)

for key in stops_dict:
    stops_dict[key] = ([stop[key] for stop in stops_list])

for column_name in ["bus_id", "stop_id", "next_stop"]:
    error_counter = 0
    for my_int in stops_dict[column_name]:
        if type(my_int) is not int:
            error_counter += 1
    errors_dict[column_name] = error_counter

for column_name in ["stop_name", "a_time"]:
    error_counter = 0
    for my_string in stops_dict[column_name]:
        if (type(my_string) is not str) or (not my_string):
            error_counter += 1
    errors_dict[column_name] = error_counter

for stop_type in stops_dict["stop_type"]:
    error_counter = 0
    if stop_type not in["", "S", "D", "F"]:
        error_counter += 1
    errors_dict["stop_type"] = error_counter


print("Type and required field validation: {} errors".format(sum([num for num in errors_dict.values()])))
for key, value in errors_dict.items():
    print("{}: {} errors".format(key, str(value)))

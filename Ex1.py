import csv
import json

from pprint import pprint
from Building import Building
from Elevator import Elevator
from ElevatorCall import ElevatorCall


def create_building_from_file(file_name):
    with open(file_name) as file:
        json_building = json.load(file)
        file.close()
    elevators = create_elevator_list_from_json(json_building["_elevators"])
    new_building = Building(min_floor=json_building["_minFloor"],
                            max_floor=json_building["_maxFloor"], elevators=elevators)
    return new_building


def create_elevator_list_from_json(elevators):
    list_of_elevators = []
    for elevator in elevators:
        new_elevator = Elevator(
            elevator_id=elevator["_id"],
            speed=elevator["_speed"],
            min_floor=elevator["_minFloor"],
            max_floor=elevator["_maxFloor"],
            close_time=elevator["_closeTime"],
            open_time=elevator["_openTime"],
            start_time=elevator["_startTime"],
            stop_time=elevator["_stopTime"]
        )
        list_of_elevators.append(new_elevator)
    return list_of_elevators


def create_list_of_call_from_csv(file_name):
    call_list = []
    csv_call_list = []
    with open(file_name) as file:
        call_list_as_csv_reader = csv.reader(file)
        for call in call_list_as_csv_reader:
            csv_call_list.append(call)

    call_parameters = {"time": 1, "source": 2, "destination": 3, "allocated_to_elevator": 5}

    for call in csv_call_list:
        new_call = ElevatorCall(
            time_of_call=call[call_parameters["time"]],
            source=call[call_parameters["source"]],
            destination=call[call_parameters["destination"]],
            allocated_to_elevator=call[call_parameters["allocated_to_elevator"]]
        )
        call_list.append(new_call)
    return call_list


def write_to_csv(list_of_calls, file_name):
    e = "Elevator call"
    csv_list_of_calls = []
    for call in list_of_calls:
        csv_list_of_calls.append([e,
                                  str(call.time_of_call),
                                  str(call.source),
                                  str(call.destination),
                                  str('0'),
                                  str(call.allocated_to_elevator)])
    with open(file_name, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(csv_list_of_calls)


def offline_algorithm(json_building_file_name, csv_list_of_calls_file_name, csv_output_file_name):
    building = create_building_from_file(json_building_file_name)
    list_of_calls = create_list_of_call_from_csv(csv_list_of_calls_file_name)
    for call in list_of_calls:
        call.allocated_to_elevator = 0
    write_to_csv(list_of_calls, csv_output_file_name)


print("3")


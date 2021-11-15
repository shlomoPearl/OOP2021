import csv
import json
import sys

from pprint import pprint
from random import randint

from Building import Building
from Elevator import Elevator
from ElevatorCall import ElevatorCall


def create_building_from_file(file_name):
    with open(file_name) as file:
        json_building = json.load(file)
        file.close()
    elevators = create_elevator_list_from_json(json_building["_elevators"])
    new_building = Building(min_floor=json_building["_minFloor"],
                            max_floor=json_building["_maxFloor"],
                            elevators=elevators)
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
            time_of_call=float(call[call_parameters["time"]]),
            source=int(call[call_parameters["source"]]),
            destination=int(call[call_parameters["destination"]]),
            allocated_to_elevator=int(call[call_parameters["allocated_to_elevator"]])
        )
        call_list.append(new_call)
    return call_list


def write_to_csv(list_of_calls, file_name):
    e = "Elevator call"
    csv_list_of_calls = []
    for call in list_of_calls:
        string_list = [
            e,
            str(call.time_of_call),
            str(call.source),
            str(call.destination),
            '0',
            str(call.allocated_to_elevator)]
        csv_list_of_calls.append(string_list)
    with open(file_name, 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(csv_list_of_calls)


def stop_cycle_time(elevator):
    return elevator.stop_time + elevator.start_time + elevator.open_time + elevator.close_time


def call_waiting_time(call: ElevatorCall, elevator: Elevator):
    source_index = elevator.queue.index(call.source)
    copy = elevator.queue[:source_index + 1]
    number_of_stops = len(copy) - 1
    distance = 0
    for i in range(1, len(copy)):
        distance += abs(copy[i] - copy[i - 1])
    stop_time = stop_cycle_time(elevator)
    time_to_source = (stop_time * number_of_stops) + (distance / elevator.speed)
    return time_to_source - call.time_of_call

def call_travel_time(call: ElevatorCall, elevator: Elevator):
    source_index = elevator.queue.index(call.source)
    destination_index = elevator.queue.index(call.destination)
    for i in range(source_index, destination_index + 1):

    distance = distance(source_index, destination_index)
    number_of_stops = stop_count(source_index, destination_index)
    return


def offline_algorithm(json_building_file_name, csv_input_file_name, csv_output_file_name):
    building = create_building_from_file(json_building_file_name)
    list_of_calls = create_list_of_call_from_csv(csv_input_file_name)

    for call in list_of_calls:
        call_direction = ""
        if call.source < call.destination:
            call_direction = 'up'
        else:
            call_direction = 'down'

        invalid_down_call = ((call_direction == 'down') and
                             ((call.destination < building.min_floor) or(call.source > building.max_floor)))
        invalid_up_call = ((call_direction == 'up') and
                           ((call.destination > building.max_floor) or (call.source < building.min_floor)))

        if invalid_up_call or invalid_down_call:
            return


    for call in list_of_calls:
        call.allocated_to_elevator = randint(1, 5)

    write_to_csv(list_of_calls, csv_output_file_name)


def main():
    files = {"json_building_file_name": 0, "csv_input_file_name": 1, "csv_output_file_name": 2}
    file_names = sys.argv[1:]
    offline_algorithm(file_names[files["json_building_file_name"]],
                      file_names[files["csv_input_file_name"]],
                      file_names[files["csv_output_file_name"]])


if __name__ == '__main__':
    main()
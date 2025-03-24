from externalstorageinterface import ExternalStorageInterface
import csv
import os

class CsvInterface(ExternalStorageInterface):
    def __init__(self, file_path=None):
        self.file_path = file_path

    def set_file_path(self, file_path):
        self.file_path = file_path

    def pull_from_storage(self):
        if self.file_path == None:
            print("No file set")
            return
        dict = {}
        with open(self.file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(csvreader):
                if i == 0:
                    keys = row[1:]
                else:
                    for j, val in enumerate(row):
                        if j == 0:
                            key = val
                            if key != "ExpPayload" and key != "PermPayload":
                                dict[key] = {}
                        else:
                            if key == "ExpPayload" or key == "PermPayload":
                                dict[key] = val
                                break
                            else:
                                dict[key][keys[j-1]] = val
        return dict

    def push_to_storage(self, data: dict):
        if self.file_path == None:
            print("No file set")
            return
        folder = '/'.join(self.file_path.split('/')[:-1])+'/'
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(self.file_path, "w", newline="") as file:
            writer = csv.writer(file)
            header = ['', 'Takeoff', 'Accel', 'Climb1', 'Cruise1', 'Patrol1', 'Service1', 'Patrol2', 'Service2', 'Patrol3', 'Service3', 'Climb2', 'Cruise2', 'Loiter', 'Landing']
            row_dict = {key: i for i, key in enumerate(header)}
            writer.writerow(header)
            for key1, dict in data.items():
                if key1 == "ExpPayload" or key1 == "PermPayload":
                    writer.writerow([key1, data[key1]])
                else:
                    row = [0 for h in header]
                    row[0] = key1
                    for key2, val in dict.items():
                        row[row_dict[key2]] = (data[key1][key2])
                    writer.writerow(row)

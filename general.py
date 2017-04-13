import csv
import json

def csv_to_json_txt(input_name, id_name):
    file_def = {'primary_id': id_name}
    body_request_template = {"action": "CREATE", "recordId": None, "record": {}}
    output_name = input_name.split(",")[0] + '.txt'
    with open(input_name) as csvfile:
        with open(output_name, 'w') as file_handle_out:
            content = csv.reader(csvfile)
            for num_line, line in enumerate(content):
                if num_line == 0:
                    simple_header = line
                    print simple_header
                else:
                    # For each line in the raw file, transform that line into a json dict.
                    record = {simple_header[n]: [data] for n, data in enumerate(line) if data}
                    body_request_template['record'] = record
                    body_request_template['recordId'] = record[file_def['primary_id']][0]
                    # And write that json dict to disk.
                    json.dump(body_request_template, file_handle_out)
                    file_handle_out.write('\n')


if __name__ == "__main__":
    name_input = raw_input("File name: ")
    id_input = raw_input("Primary ID: ")
    csv_to_json_txt(name_input, id_input)
    print('done')

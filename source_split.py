import csv
import json

def csv_to_json_txt(input_name, folder_name, id_name):
    file_def = {'primary_id': id_name}
    body_request_template = {"action": "CREATE", "recordId": None, "record": {}}
    output_dict  = {}
    with open(input_name) as csvfile:
        content = csv.reader(csvfile)
        for num_line, line in enumerate(content):
            if num_line == 0:
                simple_header = line
            else:
                # For each line in the raw file, transform that line into a json dict.
                record = {simple_header[n]: [data] for n, data in enumerate(line) if data}
                body_request_template['record'] = record
                body_request_template['recordId'] = record[file_def['primary_id']][0]
                # And write that json dict to disk.
                if len(record['source']) != 1:
                    raise ValueError('Must only have one source. Not: ' + record)
                else:
                    the_source = record['source'][0]
                try:
                    output_name = output_dict[the_source]
                except KeyError:
                    new_file = '_'.join(the_source.split()) + '.txt'
                    output_dict[the_source] = './{}/{}'.format(folder_name, new_file)
                    print('CREATED {} in DIRECTORY {}.'.format(new_file, folder_name))
                    output_name = output_dict[the_source]
                with open(output_name, 'a') as file_handle_out:
                    json.dump(body_request_template, file_handle_out)
                    file_handle_out.write('\n')

if __name__ == "__main__":
    folder_input = raw_input('Folder Name: ')
    name_input = raw_input("File name: ")
    id_input = raw_input("Primary ID: ")
    csv_to_json_txt(name_input, folder_input, id_input)
    print('\nSOURCE SPLIT COMPLETE.')
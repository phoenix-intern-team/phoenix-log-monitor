import json
import os

directory = 'C:\\Users\\320053825\\Documents\\phoenix-log-monitor\\log_files\\phoenix-log-monitor_logfiles'

json_data_audit = []
json_data_server = []
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith(".log"):
        with open('\\'.join([directory, filename]), 'r') as f:
            try:
                for line in f:
                    json_parse = json.loads(line)
                    if 'audit' in json_parse:
                        json_data_audit.append(json.loads(line))
                    else:
                        json_data_server.append(json_parse)
                # json_data_audit=[json.loads(line) for line in f if 'audit' in json.loads(line)]
                # json_data_server=[json.loads(line) for line in f if 'audit' not in json.loads(line)]
            except json.decoder.JSONDecodeError as e:
                continue

write_file_audit = open("audit-log.txt", "w")
write_file_audit.write('\n'.join(map(str, json_data_audit)))
write_file_audit.close()

write_file_server = open("server-log.txt", "w")
write_file_server.write('\n'.join(map(str, json_data_server)))
write_file_server.close()

# json_data = []
# with open ('audit-log.txt','r') as f:
#     json_data=[json.loads(line) for line in f]

# print(json_data)
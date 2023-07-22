import time
import os
import sys

path_from = sys.argv[1]


def read_from_file(*path_to_files):
    if path_to_files is not None:
        for path in path_to_files:
            server_file = open(path, 'r')
            server_configuration = server_file.read()
        print(server_configuration)
        server_file.close()


def write_to_file(*path_to_files):
    if path_to_files is not None:
        for path in path_to_files:
            server_file = open(path, 'w')
            title = "DEVELOPER MODE\n"
            server_file.write(title)
            server_params = ["CPU=20\n", "RAM=32GB\n", "TOTAL DISK=3\n", "\t/dev/sdb, /dev/sdb, /dev/sdb\n"]
            server_file.write(''.join(server_params))
        server_file.close()


start_time = time.localtime()
print("Local time: {}:{}:{}".format(start_time.tm_hour, start_time.tm_min, start_time.tm_sec))

stage = os.getenv("STAGE", default="dev").upper()

if stage.startswith("PROD*"):
    output = f"SERVER is in {stage} mode"
    print(output)
    exit()
elif os.path.exists(path_from):
    read_from_file(path_from)
else:
    write_to_file(path_from)

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)
print("Script stopped at: {}".format(time.strftime('%X', stop_time)))
print("Total runtime: {} seconds".format(difference))

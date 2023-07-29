import subprocess

run_shell = subprocess.run(['ls', './'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

test = str(run_shell.stdout.decode().split('\n'))

for element in test:
    if not element:
        continue
    print(f"plik: {element}")
print("Info{}".format(run_shell.stderr.decode()))

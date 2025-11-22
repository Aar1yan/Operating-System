import subprocess

scripts = ['task 1 script1.py', 'task 1 script2.py', 'task 1 script3.py']

for script in scripts:
    print(f"Executing {script}...")
    subprocess.call(['python3', script])
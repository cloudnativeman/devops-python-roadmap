import subprocess

pytest_result = subprocess.run(["pytest"], capture_output=True, text=True)
flake8_result = subprocess.run(["flake8", "."], capture_output=True, text=True)
print("Pytest Results:\n", pytest_result.stdout)
print("Flake8 Results:\n", flake8_result.stdout)
import requests

error_count = 0
with open("app.log") as f:
    for line in f:
        if "ERROR" in line:
            error_count += 1

if error_count > 10:
    payload = {"text": f"High error count: {error_count}"}
    requests.post("https://hooks.slack.com/services/your/webhook/url", json=payload)
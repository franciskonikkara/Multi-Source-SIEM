import json
import os
import uuid
from datetime import datetime

LOG_FILE = "cloud-simulation/logs/aws_cloudtrail.json"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def write_aws_log(user, city, ip):
    event = {
        "@timestamp": datetime(2026, 1, 9, 10, 0, 0).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "event_id": str(uuid.uuid4()),
        "user": user,
        "city": city,
        "source_ip": ip,
        "action": "ConsoleLogin",
        "status": "Success"
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

write_aws_log("admin", "New York", "1.1.1.1")
write_aws_log("admin", "London", "8.8.8.8") # Simulate "Impossible Travel"
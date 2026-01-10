import json
import time
import os
import uuid
from datetime import datetime

LOG_DIR = os.path.join("cloud-simulation", "logs")
LOG_FILE = os.path.join(LOG_DIR, "aws_cloudtrail.json")

def write_cloud_log(user, ip, location, status):
    event = {
        "@timestamp": datetime(2026, 1, 9, 12, 0, 0).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "event_id": str(uuid.uuid4()),
        "user": user,
        "source_ip": ip,
        "city": location,
        "event_source": "aws.cloudtrail",
        "action": "ConsoleLogin",
        "status": status
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")
    print(f"[+] AWS Log Generated: {user} from {location}")

if __name__ == "__main__":
    if not os.path.exists(LOG_DIR): os.makedirs(LOG_DIR)
    
    # Simulate Impossible Travel
    write_cloud_log("admin_user", "1.1.1.1", "New York", "Success")
    time.sleep(2)
    write_cloud_log("admin_user", "88.88.88.88", "London", "Success") # Impossible speed!

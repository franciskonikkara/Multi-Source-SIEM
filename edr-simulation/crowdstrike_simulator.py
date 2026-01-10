import json
import time
import os
import uuid
import random
from datetime import datetime, timedelta

LOG_DIR = os.path.join("edr-simulation", "logs")
LOG_FILE = os.path.join(LOG_DIR, "edr_events.json")

def generate_backdated_time():
    # Choose between Jan 8 and Jan 9
    chosen_day = random.choice([8, 9])
    # Pick a random hour, minute, and second
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    
    dt = datetime(2026, 1, chosen_day, hour, minute, second)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

def write_continuous_logs():
    event_types = ["process_creation", "network_connection", "memory_injection", "dns_query", "failed_login"]
    hostnames = ["DB-PROD-01", "WEB-SRV-02", "WS-USER-99"]
    
    print(f"[*] Starting continuous backdated logging (Jan 8 & 9)...")
    print(f"[*] Press Ctrl+C to stop.")

    while True:
        # Determine Severity
        severity_roll = random.random()
        if severity_roll > 0.9:
            severity = "critical"
            msg = "THREAT DETECTED: Malicious activity identified."
        elif severity_roll > 0.7:
            severity = "warning"
            msg = "Suspicious activity flagged for review."
        else:
            severity = "informational"
            msg = "Routine system telemetry."

        event = {
            "@timestamp": generate_backdated_time(),
            "event_id": str(uuid.uuid4()),
            "hostname": random.choice(hostnames),
            "event_type": random.choice(event_types),
            "severity": severity,
            "message": msg
        }

        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(event) + "\n")
            f.flush()
            os.fsync(f.fileno())

        print(f"[+] Logged {event['event_type']} for {event['@timestamp']}")
        
        # Adjust sleep to control how fast logs are generated
        time.sleep(2)

if __name__ == "__main__":
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    write_continuous_logs()
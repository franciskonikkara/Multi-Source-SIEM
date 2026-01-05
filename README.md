# Multi-Source SIEM with ELK, CrowdStrike Simulation, Splunk, AWS & Azure
Build a realistic, multi-source SIEM environment that ingests, correlates, and visualizes security telemetry from endpoints, cloud platforms, and applications while simulating EDR and cloud-native security signals.

This project implements a realistic, multi-source SIEM environment that ingests, correlates, and analyzes security telemetry from:

  Endpoint logs (Linux auth & audit logs)

  EDR telemetry (CrowdStrike-style simulated events)

  Cloud platforms (AWS CloudTrail & Azure Activity Logs)

  Multiple SIEM platforms (Elastic Stack + Splunk)

The lab is designed to simulate real SOC workflows, including detection engineering, alert triage, incident investigation, and the generation of compliance evidence.

### Objectives
Operate and tune SIEM pipelines using ELK Stack
Simulate EDR events similar to CrowdStrike Falcon
Ingest and analyze AWS & Azure security logs
Correlate events across endpoint, EDR, and cloud sources
Build detections and alerts with SOC-ready logic
Map logging and monitoring to SOC 2 & ISO/IEC 27001 controls

### Architecture Overview

Linux Endpoint
 ├── /var/log/auth.log
 ├── auditd events
 └── Simulated EDR telemetry
        ↓
Beats + Custom Collectors
        ↓
Logstash Pipelines
        ↓
Elastic SIEM (Primary)
        ↓
Kibana Dashboards & Alerts
        ↓
Splunk (Secondary SIEM View)

Cloud Logs
 ├── AWS CloudTrail + VPC Flow Logs
 └── Azure Activity Logs

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

## 📝 Overview

This project is a high-fidelity Security Information and Event Management (SIEM) laboratory. It replicates an enterprise SOC environment by ingesting telemetry from Linux Endpoints, Simulated EDR (CrowdStrike-style), and Multi-Cloud (AWS/Azure) sources into a dual-SIEM architecture (ELK + Splunk).

The primary goal is to demonstrate Detection Engineering and Data Normalization skills across disparate log formats.

## 🏗️ Architecture

The lab utilizes a "Data Lakehouse" approach:

  Collection: Filebeat and Auditbeat ship system-level events.

  Ingestion & Transformation: Logstash pipelines parse raw JSON/Syslog into Elastic Common Schema (ECS).

  Storage & Analysis: Elasticsearch acts as the primary hot-storage, with Kibana providing the visualization layer.

  Cross-Platform Visibility: Key alerts are forwarded to a Splunk instance to demonstrate multi-vendor SIEM integration.

## 🛠️ Key Features & Detections
1. Endpoint Threat Hunting

    Auditd Correlation: Monitors for execution of discovery commands (e.g., whoami, netstat) mapped to MITRE ATT&CK T1033.

    Brute Force Detection: Logstash filters identify 5+ failed SSH attempts from the same IP within 60 seconds.

2. Cloud Security (AWS/Azure)

    IAM Anomaly: Detects ConsoleLogin without MFA from CloudTrail logs.

    Azure Activity Logs: Monitors for unauthorized "Resource Group" deletions.

3. EDR Simulation

    The edr-simulation/ suite generates synthetic telemetry mimicking advanced memory-resident attacks (Process Injection, LSASS Dumping).

   

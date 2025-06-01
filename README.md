# Magma + SigScale OCS Integration Demo

This demo shows how to integrate Magma v1.9.0 with SigScale OCS for online charging.

## Prerequisites
- Docker
- Docker Compose
- Python 3.x

## Setup Instructions

### 1. Start Magma SessionD
```bash
cd magma-config
docker compose up -d
```

### 2. Start SigScale OCS
```bash
cd ocs-config
docker compose up -d
```

### 3. Verify Services
Check containers are running:
```bash
docker ps
```

You should see:
- `magma-sessiond`
- `ocs-container`

### 4. Test Charging System
```bash
cd test-scripts
python simulate_traffic.py
```

### 5. View Logs
Magma logs:
```bash
docker logs magma-config-magma-sessiond-1
```

OCS logs:
```bash
docker logs ocs-config-ocs-1
```

## Expected Outcome
1. UE session creation request sent to Magma
2. Magma initiates Diameter CCR message to OCS
3. OCS responds with quota allocation
4. Traffic usage reported back to OCS

## Troubleshooting
See [troubleshooting guide](docs/TROUBLESHOOTING.md)

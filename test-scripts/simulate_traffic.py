#!/usr/bin/env python3
# Simple UE traffic simulator
import requests
import time

MAGMA_URL = "http://localhost:8080"

def create_session(imsi):
    """Simulate UE session creation"""
    response = requests.post(
        f"{MAGMA_URL}/session/create",
        json={"imsi": imsi, "apn": "internet"}
    )
    return response.json()

def generate_traffic(imsi, megabytes):
    """Simulate data usage"""
    response = requests.post(
        f"{MAGMA_URL}/session/traffic",
        json={"imsi": imsi, "volume": megabytes * 1024 * 1024}
    )
    return response.json()

def main():
    imsi = "IMSI1234567890"
    print("Creating session...")
    session = create_session(imsi)
    print(f"Session created: {session['session_id']}")
    
    print("Simulating 10MB traffic...")
    traffic = generate_traffic(imsi, 10)
    print(f"Used {traffic['used_quota']} bytes")
    
    print("Checking OCS interactions in logs")

if __name__ == "__main__":
    main()

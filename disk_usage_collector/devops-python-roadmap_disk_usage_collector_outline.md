# Project 5: Disk Usage Collector

## Goal
SSH into multiple servers to collect and print disk usage stats.

## Steps
1. Read list of server IPs/usernames.
2. SSH into each server using paramiko.
3. Run `df -h` and collect output.

## Learning Points
- SSH automation (`paramiko`)
- Iterating over servers
- Remote command execution
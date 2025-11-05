#!/bin/bash
# projects/nmap-lab/code/scan_examples.sh
# Example Nmap scans for the lab
# Usage: ./scan_examples.sh 192.168.56.20

TARGET=${1:-192.168.1.102}
LAB_NET="192.168.1.0/24"

echo "1) Ping sweep to discover live hosts on ${LAB_NET}"
nmap -sn ${LAB_NET} -oN ../code/nmap_ping_sweep.txt

echo
echo "2) TCP SYN scan + version detection on ${TARGET}"
nmap -sS -sV -p- ${TARGET} -oN ../code/nmap_syn_fullports_${TARGET}.txt

echo
echo "3) Top ports + scripts (aggressive, lab-only)"
nmap -A --top-ports 100 ${TARGET} -oN ../code/nmap_aggressive_${TARGET}.txt

echo
echo "4) Save XML output for automation / parsing"
nmap -sS -sV -p22,80,443 ${TARGET} -oX ../code/nmap_${TARGET}.xml

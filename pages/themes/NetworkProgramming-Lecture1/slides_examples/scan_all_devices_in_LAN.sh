#!/bin/bash
for ip in 192.168.211.{1..254}; do
  ping -c 1 -W 1 $ip | grep "64 bytes" &
done
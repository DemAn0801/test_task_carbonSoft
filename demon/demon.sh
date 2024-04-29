#!/bin/sh

while true
do
x=$( (cat /proc/loadavg) | cut -c1-4)
curl --location 'http://127.0.0.1:8000/post/' \
--header 'Content-Type: application/json' \
--data '{
    "cpu": '"$x"'
}'
sleep 10
done
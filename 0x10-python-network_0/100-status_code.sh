#!/bin/bash
# happy stuff

curl -sw "%{http_code}" "$1" -o /dev/null
 
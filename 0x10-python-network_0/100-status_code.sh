#!/bin/bash
# happy stuff

curl -sLw "%{http_code}" "$1" -o /dev/null

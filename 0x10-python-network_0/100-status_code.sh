#!/bin/bash
# happy stuff

curl -sL -w "%{http_code}" "$1" -o /dev/null

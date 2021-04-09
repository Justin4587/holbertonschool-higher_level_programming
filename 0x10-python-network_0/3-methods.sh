#!/bin/bash
# putting a happy little comment right here
curl -sI "$1" | awk '/Allow:/{print $0}' | cut -d ' ' -f2-

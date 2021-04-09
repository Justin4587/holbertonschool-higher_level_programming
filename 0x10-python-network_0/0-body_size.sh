#!/bin/bash
# putting a happy little comment right here
curl -sI "$1" | awk '/Content-L/{print $2}'

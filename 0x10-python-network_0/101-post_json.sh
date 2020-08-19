#!/bin/bash
# cURL a JSON file
curl -sX POST -H "Content-Type: application/json" $1 -d @$2

#!/bin/bash
find /m${1}/MB2/ -name db |awk -F '/' '{print $(NF-1)}' >${1}occpied.TXT

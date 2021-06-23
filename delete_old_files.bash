#!/bin/bash
# Author: Imran Afzal
# Date: 22/06/2021
# Description: This script will delete all old files (+30 days) in a specific directory
# Modified: 22/06/2021

find /Users/farzandb/Downloads -mtime +30 -exec rm -r {} \;
#                                               ls -l \;
#                                               mv {} {}.old \;


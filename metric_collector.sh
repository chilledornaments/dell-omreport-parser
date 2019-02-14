#!/usr/bin/env bash

##########################################################################################################
#
#  This script runs the various Python scripts to collect metrics
# 
#  Hourly cron example for repo downloaded to /opt/ :
#  4 * * * * root /opt/dell-omreport-parser/metric_collector.sh >> /opt/dell-omreport-parser/cron.log 2>&1
#  
#  The crons should be run at different times to prevent overloading the API
#
#
#
##########################################################################################################

DIR=$(dirname $0)
SCRIPT_DIR="${DIR}"/omsa-scripts

if [ ! -d "${DIR}"/logs ]
then
mkdir "${DIR}"/logs
fi
LOG_FILE="${DIR}"/logs/$(date +%b-%d-%Y)

START_TIME=$(date +%b-%d-%Y-%H:%M:%S)

echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "Starting metrics collection" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "${START_TIME}" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"

# Run scripts
echo "Collecting fans at $(date +%H:%M:%S)" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
"${SCRIPT_DIR}"/fans.py >> "${LOG_FILE}" 
sleep 2
echo "Collecting memory at $(date +%H:%M:%S)" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
"${SCRIPT_DIR}"/memory.py >> "${LOG_FILE}"
echo "Collecting nics at $(date +%H:%M:%S)" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
sleep 2
"${SCRIPT_DIR}"/nics.py >> "${LOG_FILE}"
echo "Collecting power_supplies at $(date +%H:%M:%S)" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
sleep 2
"${SCRIPT_DIR}"/power_supplies.py >> "${LOG_FILE}"
echo "Collecting processors at $(date +%H:%M:%S)" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
sleep 2
"${SCRIPT_DIR}"/processors.py >> "${LOG_FILE}"
echo "Collecting temps at $(date +%H:%M:%S)" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
sleep 2
"${SCRIPT_DIR}"/temps.py >> "${LOG_FILE}"
echo "Collecting pdisk at $(date +%H:%M:%S)" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
sleep 2
"${SCRIPT_DIR}"/pdisk.py >> "${LOG_FILE}"
echo "Collecting vdisk at $(date +%H:%M:%S)" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
sleep 2
"${SCRIPT_DIR}"/vdisk.py >> "${LOG_FILE}"
sleep 2
END_TIME=$(date +%b-%d-%Y-%H:%M:%S)
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "Finished metrics collection" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "${END_TIME}" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"
echo "********************************" >> "${LOG_FILE}"
echo "" >> "${LOG_FILE}"

exit 0


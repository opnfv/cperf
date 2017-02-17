#!/bin/bash

pwd
echo "Workspace:" $WORKSPACE
echo "Job name:" $JOB_NAME
echo "Starting new test with Build Number= "$BUILD_NUMBER

#export RESULTS_DIR=$JOB_NAME"_"$BUILD_NUMBER
/etc/init.d/tomcat6 start
/usr/bin/mysqld_safe > /dev/null 2>&1 &
echo "startup...."

#mkdir -p /home/pktblastersdn/Results/$JOB_NAME"_"$BUILD_NUMBER
mkdir -p /home/pktblastersdn/Results

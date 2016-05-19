##############################################################################
# Docker container for CPerf's test tools.
##############################################################################
#
# To build (from the directory that contains this Dockerfile):
#   $ docker build -t opnfv/cperf .
#
# To run:
#   $ docker run -it opnfv/cperf ${pybot_command}
#
# Pass the full pybot test command as ${pybot_command}.
#
# Copyright (c) 2016 Red Hat Inc.
# Jamo Luhrsen <jluhrsen@redhat.com>
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
#############################################################################

FROM centos:7
MAINTAINER Jamo Luhrsen <jluhrsen@redhat.com>

ENV HOME /home/opnfv
ENV REPOS_DIR /home/opnfv/repos
RUN mkdir -p ${REPOS_DIR}

RUN yum install -y epel-release && yum update -y

RUN yum install -y \
    net-snmp-devel \
    libpcap-devel \
    autoconf \
    make \
    automake \
    libtool \
    libconfig-devel \
    libffi-devel \
    wget \
    git \
    python-devel \
    python-pip \
    python-setuptools

RUN pip install docker-py \
    setuptools \
    importlib \
    requests \
    scapy \
    netifaces \
    netaddr \
    ipaddr \
    jsonpath-rw \
    robotframework{,-{httplibrary,requests,sshlibrary,selenium2library}}

RUN git config --global http.sslVerify false

# Clone ODL Int/Test, ODL RelEng and OPNFV CPerf repos
ENV CPERF_REPO_DIR ${REPOS_DIR}/cperf
ENV RELENG_REPO_DIR ${REPOS_DIR}/releng
ENV ODL_TEST_REPO_DIR ${REPOS_DIR}/odl_test
RUN git clone https://gerrit.opnfv.org/gerrit/cperf ${CPERF_REPO_DIR}
RUN git clone https://gerrit.opnfv.org/gerrit/releng ${RELENG_REPO_DIR}
RUN git clone https://git.opendaylight.org/gerrit/p/integration/test ${ODL_TEST_REPO_DIR}

# Clone and build CBench
ENV OF_DIR ${REPOS_DIR}/openflow
ENV OFLOPS_DIR ${REPOS_DIR}/oflops
RUN git clone git://gitosis.stanford.edu/openflow.git ${OF_DIR}
RUN git clone https://github.com/andi-bigswitch/oflops.git ${OFLOPS_DIR}
RUN cd ${OFLOPS_DIR} && ./boot.sh && ./configure --with-openflow-src-dir=${OF_DIR} && make && make install

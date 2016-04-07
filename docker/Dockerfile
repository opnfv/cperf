##############################################################################
#   Docker container for CPERF
##############################################################################
# Purpose:  tools container to execute CPERF related tests.  Opendaylight
#           system tests are included and could be called by running a
#           similar commands:
#
#               $ docker build -t opnfc/cperf:${tag} .
#               $ docker run -t -i opnfv/cperf ${pybot_command}
#
#               where ${tag} would likely be "latest" and the ${pybot_command}
#               would be the entire command line for a robot framework test.
#
#
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
LABEL image=opnfv/cperf

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
    wget \
    git \
    python-devel \
    python-pip \
    python-setuptools && \
    easy_install -U setuptools

RUN pip install -q docker-py \
    importlib \
    requests \
    scapy \
    netifaces \
    netaddr \
    ipaddr \
    jsonpath-rw \
    robotframework{,-{httplibrary,requests,sshlibrary,selenium2library}}

RUN git config --global http.sslVerify false

# clone the test code
ENV CPERF_REPO_DIR ${REPOS_DIR}/cperf
ENV RELENG_REPO_DIR ${REPOS_DIR}/releng
ENV ODL_TEST_REPO ${REPOS_DIR}/odl_test
RUN git clone https://gerrit.opnfv.org/gerrit/cperf ${CPERF_REPO_DIR}
RUN git clone https://gerrit.opnfv.org/gerrit/releng ${RELENG_REPO_DIR}
RUN git clone https://git.opendaylight.org/gerrit/p/integration/test ${ODL_TEST_REPO}

# build cbench
ENV OF_DIR ${REPOS_DIR}/openflow
ENV OFLOPS_DIR ${REPOS_DIR}/oflops
RUN git clone git://gitosis.stanford.edu/openflow.git ${OF_DIR}
RUN git clone https://github.com/andi-bigswitch/oflops.git ${OFLOPS_DIR}
RUN cd ${OFLOPS_DIR} && ./boot.sh && ./configure --with-openflow-src-dir=${OF_DIR} && make && make install
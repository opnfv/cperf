FROM centos:7

LABEL image=opnfv/cperf

# GIT repo directory
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

ENV CPERF_REPO_DIR ${REPOS_DIR}/cperf
ENV RELENG_REPO_DIR ${REPOS_DIR}/releng
ENV ODL_TEST_REPO ${REPOS_DIR}/odl_test
RUN git clone https://gerrit.opnfv.org/gerrit/cperf ${CPERF_REPO_DIR}
RUN git clone https://gerrit.opnfv.org/gerrit/releng ${RELENG_REPO_DIR}
RUN git clone https://git.opendaylight.org/gerrit/p/integration/test ${ODL_TEST_REPO}

ENV OF_DIR ${REPOS_DIR}/openflow
ENV OFLOPS_DIR ${REPOS_DIR}/oflops
RUN git clone git://gitosis.stanford.edu/openflow.git ${OF_DIR}
RUN git clone https://github.com/andi-bigswitch/oflops.git ${OFLOPS_DIR}
RUN cd ${OFLOPS_DIR} && ./boot.sh && ./configure --with-openflow-src-dir=${OF_DIR} && make && make install
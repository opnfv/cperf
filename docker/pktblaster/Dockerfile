##############################################################################
# Docker container for PktblasterSDN test tools.
##############################################################################
#
# To build (from the directory that contains this Dockerfile):
#   $ docker build -t pktblastersdn .
#
# To run:
#   $ docker run -it pktblastersdn
#
#############################################################################

FROM centos:7
MAINTAINER Hemankumar

ENV PBSDN_DIR /home/pktblastersdn
RUN mkdir -p ${PBSDN_DIR}
ARG RPM_PACK_NAME=PBSDN-1.4.4.0-1.el7.centos.x86_64.rpm
ARG RPM_REPO_URL=http://artifacts.opnfv.org/cperf/pktblaster/

RUN yum install -y epel-release && yum update -y

RUN yum install -y \
    psmisc \
    telnet \
    net-tools \
    mlocate \
    sudo \
    curl \
    openssl \
    gcc \
    make \
    python-devel \
    openssl-devel \
    kernel-devel \
    graphviz \
    kernel-debug-devel \
    autoconf \
    automake \
    libtool \
    xorg-x11-xauth \
    python-six \
    deltarpm \
    dmidecode \
    iproute \
    python-requests \
    python-netaddr \
    libpcap-devel \
    gtk3-devel \
    c-ares-devel

#-------------------------------------------------------------------------------
# Mysql
#-------------------------------------------------------------------------------
RUN rpm -Uvh http://repo.mysql.com/mysql-community-release-el7-7.noarch.rpm
RUN yum install -y mysql-server
RUN mysql --version
RUN chown -R mysql:mysql /var/lib/mysql
RUN mysql_install_db --user=mysql --ldata=/var/lib/mysql
RUN /usr/bin/mysqld_safe & \
    sleep 10s &&\
    echo "use mysql; update user set password=PASSWORD(\"ATTEST\") where User='root'; FLUSH PRIVILEGES" | mysql

EXPOSE 3306 80

#-------------------------------------------------------------------------------
# PKTBLASTER-SDN
#-------------------------------------------------------------------------------
ADD ./pktblastersdn_startup.sh ${PBSDN_DIR}/
RUN chmod +x ${PBSDN_DIR}/pktblastersdn_startup.sh

#---------------------------------------------------------------------------------------
# get rpm from external "artifacts.opnfv.org/cperf/pktblaster" repo to container. 
# if this enable,below local ADD should be disabled
#---------------------------------------------------------------------------------------
RUN cd ${PBSDN_DIR}/ && curl -O $RPM_REPO_URL/$RPM_PACK_NAME && cd /root

#---------------------------------------------------------------------------------------
# move rpm from local to container, if this enable, external repo RUN should be disabled
#---------------------------------------------------------------------------------------
#ADD ./$RPM_PACK_NAME ${PBSDN_DIR}/
RUN /usr/bin/mysqld_safe & \
    sleep 10s &&\
    rpm -Uvh ${PBSDN_DIR}/$RPM_PACK_NAME
RUN rpm -ivh /usr/local/wireshark-2.2.2-1.x86_64.rpm

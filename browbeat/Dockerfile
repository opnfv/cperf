FROM alpine

# Browbeat Install
# Install Dependencies for Alpine Linux
RUN apk add --update \
    python-dev \
    gcc \
    g++ \
    git \
    libffi-dev \
    openssl-dev \
    python2 \
    linux-headers \
    python3-dev \
    py-pip \
    make \
    && pip install virtualenv==15.2.0 \
    && pip install setuptools==38.7.0
ENV INSTALL_PATH /root/browbeat
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
RUN git clone https://github.com/openstack/browbeat.git \
    && virtualenv $INSTALL_PATH/browbeat/.browbeat-venv \
    && source $INSTALL_PATH/browbeat/.browbeat-venv/bin/activate \
    && pip install -r $INSTALL_PATH/browbeat/requirements.txt \
# Browbeat's PerfKitBenchmarker Install
    && virtualenv $INSTALL_PATH/browbeat/.perfkit-venv \
    && cd $INSTALL_PATH/browbeat/.perfkit-venv \
    && git clone https://github.com/GoogleCloudPlatform/PerfKitBenchmarker.git \
    && source $INSTALL_PATH/browbeat/.perfkit-venv/bin/activate \
    && pip install -r $INSTALL_PATH/browbeat/.perfkit-venv/PerfKitBenchmarker/requirements.txt \
    && pip install -r $INSTALL_PATH/browbeat/.perfkit-venv/PerfKitBenchmarker/perfkitbenchmarker/providers/openstack/requirements.txt \
    && pip install openstacksdk==0.9.17 \
    && pip install python-openstackclient==3.12.0 \
    && pip install python-novaclient==9.1.0 \
# Browbeat's Rally Install
    && virtualenv $INSTALL_PATH/browbeat/.rally-venv \
    && echo 'export PYTHONPATH=$PYTHONPATH:$INSTALL_PATH/browbeat' >> $INSTALL_PATH/browbeat/.rally-venv/bin/activate \
    && source $INSTALL_PATH/browbeat/.rally-venv/bin/activate \
    && pip install rally==0.10.1 \
    && pip install gnocchiclient==3.3.1 \
    && pip install elasticsearch \
# Browbeat's Shaker Install
    && virtualenv $INSTALL_PATH/browbeat/.shaker-venv \
    && source $INSTALL_PATH/browbeat/.shaker-venv/bin/activate \
    && pip install pyshaker==1.1.0
WORKDIR $INSTALL_PATH/browbeat/

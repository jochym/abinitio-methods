#!/bin/bash

exit 0

# Build and install ALAMODE
RUN git clone http://github.com/ttadano/alamode.git
WORKDIR alamode
RUN mkdir build && cd build && cmake .. 
RUN cd build && make alm 
RUN cd build && make anphon 
RUN cd build/tools && make 

# Install alamode
USER root
RUN cp build/alm/alm build/anphon/anphon build/tools/{analyze_phonons,qe2alm,dfc2,fc_virtual} /usr/local/bin/
RUN cp tools/*.py /usr/local/bin
RUN chmod a+x /usr/local/bin/*.py
RUN apt-get autoremove -y g++ cmake
RUN cd .. && ls -l $HOME/alamode

USER jovyan
WORKDIR $HOME

# Import the workspace into JupyterLab
RUN jupyter lab workspace import workspace-gp.json

# Set up the abinit program and data
#ENV ABINIT_PP_PATH="psp/GGA_FHI/:psp/LDA_FHI/:psp/LDA_PAW/:psp/GGA_PAW/"
ENV ABINIT_PP_PATH="/usr/share/abinit/psp:/usr/share/abinit/psp/HGH:/home/jovyan/abinitio-methods/psp"

RUN rm workspace-gp.json

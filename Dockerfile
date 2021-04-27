FROM jochym/jupyter-stacks

MAINTAINER Pawel T.  Jochym <pawel.jochym@ifj.edu.pl>

USER root

# Add dependencies
RUN sed -i 's/main/main contrib non-free/g' /etc/apt/sources.list
RUN sed -i 's/main/main contrib non-free/g' /etc/apt/sources.list.d/backports.list

RUN apt-get update
RUN apt-get -qy full-upgrade
RUN apt-get -qy install git apt-utils
RUN apt-get -qy install abinit abinit-data && apt-get clean

# Non-essential dependencies
RUN apt-get install -qy htop abinit-doc pandoc vim mc  && apt-get clean
#RUN apt-get install -qy texlive-latex-recommended texlive-fonts-recommended texlive-latex-extra && apt-get clean

# Extra dependencies
#RUN apt-get update
#RUN apt-get install -y ffmpeg && apt-get clean

RUN apt-get clean

# Conda deps
USER jovyan
RUN conda init bash
RUN conda config --show-sources
RUN conda config --system --add channels jochym
RUN conda install -y mamba
RUN mamba install -y jupyterlab
RUN mamba install -y scipy numpy matplotlib ase spglib nglview elastic phonopy \
    jupyter_contrib_nbextensions jupytext jupyter-offlinenotebook jupyterlab-python-file\
    ipywidgets nbgitpuller jupyterlab-mathjax3 rise

RUN mamba update -y --all
RUN mamba clean -y --all

# # Materials
USER root
COPY workspace-gp.json /home/jovyan/
RUN chown -R jovyan:users /home/jovyan

# Update submodules
USER jovyan
#RUN cd /home/jovyan/work && git submodule init && git submodule update
WORKDIR $HOME

#RUN jupyter labextension install \
#    @jupyterlab/katex-extension  \
#    @jupyter-widgets/jupyterlab-manager
#    @jupyter-widgets/jupyterlab-manager @jupyterlab/toc jupyterlab-jupytext  nglview-js-widgets

#RUN jupyter lab build
#RUN jupyter lab clean

# Import the workspace into JupyterLab
RUN jupyter lab workspace import workspace-gp.json

# Set up the abinit program and data
#ENV ABINIT_PP_PATH="psp/GGA_FHI/:psp/LDA_FHI/:psp/LDA_PAW/:psp/GGA_PAW/"
ENV ABINIT_PP_PATH="/usr/share/abinit/psp:/usr/share/abinit/psp/HGH:/home/jovyan/abinitio-methods/psp"

RUN rm workspace-gp.json

# Build alamode
USER root
RUN pwd
RUN git clone http://github.com/ttadano/alamode.git
WORKDIR alamode
RUN pwd && ls -l
RUN apt update 
RUN apt -q -y install libeigen3-dev libsymspg-dev g++ libopenblas-dev fftw3-dev cmake libboost-dev libopenmpi-dev
RUN mkdir build && cd build && cmake .. && make -j 
RUN cp build/alm/alm build/anphon/anphon build/tools/{analyze_phonons,qe2alm,dfc2,fc_virtual} /usr/local/bin/
RUN pwd && ls -lR build && ls -l /usr/local/bin/
RUN ldd /usr/local/bin/anphon
RUN ldd /usr/local/bin/alm

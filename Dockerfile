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
RUN conda config --show-sources
RUN conda config --add channels jochym
RUN conda install -y scipy numpy matplotlib ase spglib nglview elastic phonopy
RUN conda install -y jupyter_contrib_nbextensions 
RUN conda update -y --all
RUN conda clean -y --all

# Materials
USER root
COPY . /home/jovyan/
RUN mkdir /home/jovyan/work
RUN chown -R jovyan:users /home/jovyan

# Update submodules
USER jovyan
#RUN cd /home/jovyan/work && git submodule init && git submodule update
WORKDIR $HOME

# Import the workspace into JupyterLab
RUN jupyter lab workspaces import abinit-ws.json

# Set up the abinit program and data
#ENV ABINIT_PP_PATH="psp/GGA_FHI/:psp/LDA_FHI/:psp/LDA_PAW/:psp/GGA_PAW/"
ENV ABINIT_PP_PATH="/usr/share/abinit/psp:/usr/share/abinit/psp/HGH"

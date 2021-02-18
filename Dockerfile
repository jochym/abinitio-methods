FROM jochym/jupyter-stacks

MAINTAINER Pawel T.  Jochym <pawel.jochym@ifj.edu.pl>

USER root

# Add dependencies
RUN sed -i 's/main/main contrib non-free/g' /etc/apt/sources.list
RUN ls -lR /etc/apt/

RUN apt-get update
RUN apt-get -qy upgrade
RUN apt-get -qy install git apt-utils
RUN apt-get -qy install abinit povray imagemagick && apt-get clean

# Non-essential dependencies
RUN apt-get install -qy htop abinit-doc pandoc 
RUN apt-get install -qy texlive-latex-recommended texlive-fonts-recommended texlive-latex-extra && apt-get clean

# Extra dependencies
RUN apt-get update
RUN apt-get install -y ffmpeg && apt-get clean

RUN apt-get clean

# Conda deps
USER jovyan
RUN conda config --add channels conda-forge
RUN conda config --add channels jochym
RUN conda install -y scipy numpy matplotlib ase spglib nglview elastic phonopy
RUN conda install -y jupyter_contrib_nbextensions 
RUN conda install -y -c damianavila82 rise
RUN conda install -y -c vpython vpython vpnotebook
RUN conda update -y --all
RUN conda clean -tipsy

# Materials
USER root
COPY . /home/jovyan/work
RUN chown -R jovyan:users /home/jovyan/work

# Update submodules
USER jovyan
RUN cd /home/jovyan/work && git submodule init && git submodule update




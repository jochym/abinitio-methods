#!/bin/bash

td=`dirname "$0"`

LD_LIBRARY_PATH=/opt/conda/lib/:/opt/tljh/user/lib ${td}/anphon $*




#!/bin/bash
. /etc/profile
export PYTHONPATH=$PYTHONPATH:/data/bigdata-dq
/home/oyo_admin/miniconda3/envs/data-quality/bin/python /data/bigdata-dq/src/main.py $1
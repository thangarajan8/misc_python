# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:44:50 2019

@author: Thanga
"""

from pyathenajdbc import connect

S3_STAGING_DIR = 's3://aws-athena-query-results-333810411750-ap-south-1/'
REGION = 'ap-south-1'
conn = connect(s3_staging_dir=S3_STAGING_DIR,
               region_name=REGION)
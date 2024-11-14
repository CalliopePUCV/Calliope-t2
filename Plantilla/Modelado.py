# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:06:03 2023

@author: Patricio
"""

import calliope
import pandas as pd

model = calliope.Model('')

model.inputs
model.inputs.resource.to_pandas()
model.get_formatted_array('resource').sum('locs').to_pandas()
model.run()
model.results
#model.to_csv("csv/base.csv")

model.plot.summary()
model.plot.flows(timestep_cycle=1)


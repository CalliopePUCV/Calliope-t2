# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:06:03 2023

@author: Patricio
"""

import calliope
import pandas as pd

model = calliope.Model(r'C:\Users\patri\OneDrive\Escritorio\One drive\Tesis\codigosfinales\Prueba_Oficial_1_OFF_GRID METANOL - copia\model.yml')

#C:/Users/jorge/OneDrive/Documents/PUCV/TESIS-H2IN-PAPELERAS/MODELO BIOBIO/ESCENARIOS/ESCENARIO I - version  compresor - ONGRID/model.yml

model.inputs
model.inputs.resource.to_pandas()
model.get_formatted_array('resource').sum('locs').to_pandas()
model.run()
model.results
model.to_csv("csv/TEST1_OFFGRID_E7.3a_METANOLPARCIAL_P+D.csv")
#DAC
model.plot.summary(to_file=r'C:\Users\patri\OneDrive\Escritorio\One drive\Tesis\codigosfinales\Prueba_Oficial_1_OFF_GRID METANOL\plot\E7.3a_OFF_METANOLPARCIAL_P+D.html', mapbox_access_token='pk.eyJ1IjoiZWxyaWNoaWFyZG8iLCJhIjoiY2wxbGJxN2VxMDQ1djNpbnd1ejAxYXQ4NSJ9.CUIkq5dLLfYC4ZvDb-SOlA')
#model.plot.flows(timestep_cycle=1) 
#model.plot.capacity()
#model.plot.capacity(array='total_levelised_cost')

#costs =  model.get_formatted_array('cost').loc[{'costs': 'monetary'}].to_pandas()
#costs

#lcoes = model.results.systemwide_levelised_cost.loc[{'carriers': 'electricity', 'costs':'monetary'}].to_pandas()
#lcoes

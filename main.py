# -*- coding: utf-8 -*-
"""This will probably be a single-'class' project, its only goal is to sample a dataset"""
import shutil
from typing import Any, Union

import pandas as pd
from pandas import DataFrame, Series
from pandas.core.generic import NDFrame
from pandas.io.parsers import TextFileReader

dataset: str = './validated.tsv'
sample_size: int = 50000
random_state: int = 64
dataframe_column: str = 'path'

sample_output: str = "../sample/"

dataframe: Union[Union[TextFileReader, Series, DataFrame, None, NDFrame], Any] = pd.read_csv(dataset, sep = '\t')
sample = dataframe.sample(sample_size, replace = True, random_state = random_state)
sample_paths = sample[dataframe_column].tolist()

for i in sample_paths:
    shutil.copy2(f"./clips/{i}", sample_output)
    print(i)

# -*- coding: utf-8 -*-
"""This will probably be a single-'class' project, its only goal is to sample a dataset"""
from typing import Any, Union

import pandas as pd
from pandas import DataFrame, Series
from pandas.core.generic import NDFrame
from pandas.io.parsers import TextFileReader

cv_validated_df: Union[Union[TextFileReader, Series, DataFrame, None, NDFrame], Any] = pd.read_csv('validated.tsv', sep='\t')
print(cv_validated_df)

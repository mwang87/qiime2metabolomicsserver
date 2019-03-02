import pandas as pd
import os
import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

df = pd.read_csv(input_filename, sep="\t")

if "sample_name" in df:
    manifest_df = df["sample_name", "filename"]
else:
    #manifest_df = df["filename", "ATTRIBUTE_instrument"]
    #manifest_df = df.loc[:, ['filename']]
    manifest_df = pd.DataFrame()
    manifest_df["sample_name"] = df["filename"]
    manifest_df["filepath"] = df["filename"]

manifest_df.to_csv(output_filename, index=False, sep=",")

import pandas as pd
import os
import sys

input_metadata_filename = sys.argv[1]
input_quantification_table = sys.argv[2]
output_filename = sys.argv[3]

df_metadata = pd.read_csv(input_metadata_filename, sep="\t")
df_quantification = pd.read_csv(input_quantification_table, sep="\t")

if "sample_name" in df_metadata:
    manifest_df = df["sample_name", "filename"]
else:
    manifest_df = pd.DataFrame()
    manifest_df["sample_name"] = df_metadata["filename"]
    manifest_df["filepath"] = df_metadata["filename"]

"""Checking if the set of filenames are fully covered, if not then we'll provide a place holder"""
#TODO: FINISH

manifest_df.to_csv(output_filename, index=False, sep=",")

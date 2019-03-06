import pandas as pd
import os
import sys

input_metadata_filename = sys.argv[1]
input_quantification_table = sys.argv[2]
output_manifest_filename = sys.argv[3]
output_metadata_filename = sys.argv[4]

df_metadata = pd.read_csv(input_metadata_filename, sep="\t")
df_quantification = pd.read_csv(input_quantification_table, sep=",")

if "sample_name" in df_metadata:
    manifest_df = df_metadata["sample_name", "filename"]
else:
    manifest_df = pd.DataFrame()
    manifest_df["sample_name"] = df_metadata["filename"]
    manifest_df["filepath"] = df_metadata["filename"]

"""Checking if the set of filenames are fully covered, if not then we'll provide a place holder"""
all_quantification_filenames = [key.split(" ")[0] for key in df_quantification.keys() if "Peak area" in key]

manifest_filenames = list(manifest_df["filepath"])

manifest_object_list = manifest_df.to_dict(orient="records")
for quantification_filename in all_quantification_filenames:
    if not quantification_filename in manifest_filenames:
        print(quantification_filename, "not found")
        manifest_object = {}
        manifest_object["filepath"] = quantification_filename
        manifest_object["sample_name"] = quantification_filename
        manifest_object_list.append(manifest_object)

pd.DataFrame(manifest_object_list).to_csv(output_manifest_filename, index=False, sep=",")


"""Reformatting the metadata filename"""
if "sample_name" in df_metadata:
    new_output_metadata = df_metadata
else:
    new_output_metadata = df_metadata
    new_output_metadata["sample_name"] = df_metadata["filename"]

output_columns = list(new_output_metadata.keys())
output_columns.remove("sample_name")
output_columns.insert(0, "sample_name")
new_output_metadata.to_csv(output_metadata_filename, index=False, sep="\t", columns=output_columns)

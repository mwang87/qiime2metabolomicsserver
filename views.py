# views.py
from flask import abort, jsonify, render_template, request, redirect, url_for, send_file, make_response, send_from_directory

from app import app

import os
import csv
import json
import uuid
import requests

@app.route('/', methods=['GET'])
def renderhomepage():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def validate():
    metadata_file = request.files['metadata']
    quantification_file = request.files['quantification']
    manifest_file = request.files['manifest']

    uuid_prefix = str(uuid.uuid4())

    local_metadata_filename = os.path.join(app.config['UPLOAD_FOLDER'], uuid_prefix + "_metadata.tsv")
    local_quantification_filename = os.path.join(app.config['UPLOAD_FOLDER'], uuid_prefix + "_quantification.tsv")
    local_manifest_filename = os.path.join(app.config['UPLOAD_FOLDER'], uuid_prefix + "_manifest.tsv")

    metadata_file.save(local_metadata_filename)
    quantification_file.save(local_quantification_filename)
    manifest_file.save(local_manifest_filename)

    local_qza_table = os.path.join(app.config['UPLOAD_FOLDER'], uuid_prefix + "_table.qza")
    local_qza_distance = os.path.join(app.config['UPLOAD_FOLDER'], uuid_prefix + "_distance.qza")
    local_qza_pcoa = os.path.join(app.config['UPLOAD_FOLDER'], uuid_prefix + "_pcoa.qza")
    local_qzv_emperor = os.path.join(app.config['UPLOAD_FOLDER'], uuid_prefix + "_emperor.qzv")

    all_cmd = []
    all_cmd.append("qiime metabolomics import-mzmine2 --p-manifest %s --p-quantificationtable %s --o-feature-table %s" % (local_manifest_filename, local_quantification_filename, local_qza_table))
    all_cmd.append("qiime diversity beta \
    --i-table %s \
    --p-metric cosine \
    --o-distance-matrix %s" % (local_qza_table, local_qza_distance))
    all_cmd.append("qiime diversity pcoa \
    --i-distance-matrix %s \
    --o-pcoa %s" % (local_qza_distance, local_qza_pcoa))
    all_cmd.append("qiime emperor plot \
    --i-pcoa %s \
    --m-metadata-file %s \
    --o-visualization %s \
    --p-ignore-missing-samples" % (local_qza_pcoa, local_metadata_filename, local_qzv_emperor))

    for cmd in all_cmd:
        os.system(cmd)

    response_dict = {}
    response_dict["table_qza"] = "/cdn/" + uuid_prefix + "_table.qza"
    response_dict["emperor_qzv"] = "/cdn/" + uuid_prefix + "_emperor.qzv"

    return json.dumps(response_dict)

"""Custom way to send files back to client"""
@app.route('/cdn/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/heartbeat', methods=['GET'])
def testapi():
    return_obj = {}
    return_obj["status"] = "success"
    return json.dumps(return_obj)

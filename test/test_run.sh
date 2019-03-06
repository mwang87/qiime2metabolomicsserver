

qiime metabolomics  import-mzmine2 --p-manifest qiime2_manifest.tsv --p-quantificationtable mzmine2quant.csv --o-feature-table myqza.qza
qiime feature-table summarize --i-table myqza.qza --o-visualization myqza_summary.qzv
qiime diversity beta \
--i-table myqza.qza \
--p-metric cosine \
--o-distance-matrix myqza_distance.qza
qiime diversity pcoa \
--i-distance-matrix myqza_distance.qza \
--o-pcoa myqza_pcoa.qza
 # qiime emperor plot \
 #    --i-pcoa myqza_pcoa.qza \
 #    --m-metadata-file metadata.tsv \
 #    --o-visualization myqza_emperor.qzv \
 #    --p-ignore-missing-samples
qiime emperor plot \
--i-pcoa myqza_pcoa.qza \
--m-metadata-file qiime2_metadata.tsv \
--o-visualization myqza_emperor.qzv \
--p-ignore-missing-samples

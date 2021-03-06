__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os
import refgenconf

genome = snakemake.params.genome
asset = snakemake.params.asset
tag = snakemake.params.tag

conf_path = os.environ["REFGENIE"]

rgc = refgenconf.RefGenConf(conf_path, writable=True)

# pull asset if necessary
gat, archive_data, server_url = rgc.pull(genome, asset, tag, force=False)

for seek_key, out in snakemake.output.items():
    path = rgc.seek(genome, asset, tag_name=tag, seek_key=seek_key, strict_exists=True)
    os.symlink(path, out)

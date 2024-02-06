import logging

from app.config import (
    EDGE_DATA_PATH,
    EDGE_EPSG,
    EDGE_LOD,
    EDGE_SOURCE,
    N_RANGE,
    WFS_BASE_REQUEST,
    WFS_EPSG,
    WFS_LOD,
    WFS_URL,
)

logger = logging.getLogger("root")

from oaemlib import FileSettings, LocalGMLProvider, NRWFilePicker, WFSGMLProvider, WFSSettings

if EDGE_SOURCE == "FILE":
    file_settings = FileSettings(data_path=EDGE_DATA_PATH, epsg=EDGE_EPSG, lod=EDGE_LOD, n_range=N_RANGE)
    file_picker = NRWFilePicker(file_settings)
    gml_provider = LocalGMLProvider(file_picker)
    logger.info("Using local edge data from %s", EDGE_DATA_PATH)
else:
    wfs_settings = WFSSettings(url=WFS_URL, base_request=WFS_BASE_REQUEST, epsg=WFS_EPSG, n_range=N_RANGE, lod=WFS_LOD)
    gml_provider = WFSGMLProvider(wfs_settings=wfs_settings)
    logger.info("Using WFS edge data")

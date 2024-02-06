import numpy as np

OAEM_CACHE_SIZE = 500
OAEM_RES = np.deg2rad(5)  # resolution of the OAEM grid in radians

N_RANGE = 50  # neighborhood radius in meters

EDGE_SOURCE = "WFS"  # "WFS" or "FILE"
EDGE_DATA_PATH = "./gmldata"  # only relevant if EDGE_SOURCE == "FILE"
EDGE_LOD = 2  # 1 or 2, 2 includes roof shapes and more detailed buildings but is slower
EDGE_EPSG = 25832  # EPSG of the CityGML data source

WFS_EPSG = 25832
WFS_URL = "https://www.wfs.nrw.de/geobasis/wfs_nw_3d-gebaeudemodell_lod1"
WFS_BASE_REQUEST = "Service=WFS&REQUEST=GetFeature&VERSION=1.1.0&TYPENAME=bldg:Building"
WFS_LOD = 1

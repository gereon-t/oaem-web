import logging
import time
from typing import Optional

from fastapi import APIRouter
from fastapi.responses import Response
from oaemlib import Oaem, SunTrack, compute_oaem

from app import gml_provider
from app.cache import Cache
from app.plotting import create_json_fig

logger = logging.getLogger("root")

router = APIRouter()


def get_oaem(
    pos_x: float,
    pos_y: float,
    epsg: int,
    pos_z: Optional[float] = None,
) -> Oaem:
    """
    Returns the OAEM for a given position.

    Args:

        pos_x (float): The x-coordinate of the position.
        pos_y (float): The y-coordinate of the position.
        pos_z (float): The z-coordinate of the position.
        epsg (int): The EPSG code of the position.

    Returns:

        The OAEM for the given position.
    """
    start_time = time.time()
    oaem_cache = Cache()

    oaem_key = f"{pos_x}_{pos_y}_{pos_z}_{epsg}"

    if oaem_key in oaem_cache:
        logger.info("OAEM cache hit for key: %s", oaem_key)
        end_time = time.time()
        logger.info("Computed OAEM in %.2f seconds", end_time - start_time)
        return oaem_cache[oaem_key]

    oaem = compute_oaem(pos_x=pos_x, pos_y=pos_y, pos_z=pos_z, epsg=epsg, gml_provider=gml_provider)
    oaem_cache[oaem_key] = oaem
    end_time = time.time()
    logger.info("Computed OAEM in %.2f seconds", end_time - start_time)
    return oaem


@router.get("/oaem")
async def request_oaem(pos_x: float, pos_y: float, epsg: int, pos_z: Optional[float] = None) -> dict:
    """
    Computes the Obstruction Adaptive Elevation Mask (OAEM) for a given position and EPSG code.

    This API endpoint calculates the OAEM, which represents the obstruction of the sky view due to
    buildings using elevation angles. The OAEM is given with an azimuth resolution of 1 degree.

    Note: The OAEM data provided by this API is currently available only for the state of North Rhine-Westphalia (NRW), Germany.
    If the provided position is outside the area of operation, an empty OAEM is returned.

    Args:

        pos_x (float): The x-coordinate of the position.
        pos_y (float): The y-coordinate of the position.
        pos_z (float): The z-coordinate of the position.
        epsg (int): The EPSG code specifying the coordinate reference system (CRS) of the provided position.

    Returns:

        A JSON object with:

            - data (str): The OAEM data represented as a string in azimuth:elevation format.
                          If the position is outside the area of operation, the OAEM will be empty.
                          Azimuth and elevation are given in radians.
    """
    oaem = get_oaem(pos_x=pos_x, pos_y=pos_y, pos_z=pos_z, epsg=epsg)
    return {"data": oaem.az_el_str}


@router.get("/sunvis")
async def request_sun_visibility(pos_x: float, pos_y: float, epsg: int, pos_z: Optional[float] = None) -> dict:
    """
    Derives the sun visibility for a given position using the Obstruction Adaptive Elevation Mask (OAEM).

    The trajectory of the sun is intersected with the OAEM to determine the sun visibility for the given position.
    The sun visibility is given as a boolean value, which is true if the sun is visible and false otherwise.
    Furthermore, the time interval for the current sun visibility is given.

    Args:

            pos_x (float): The x-coordinate of the position.
            pos_y (float): The y-coordinate of the position.
            pos_z (float): The z-coordinate of the position.
            epsg (int): The EPSG code of the position.

    Returns:

            A JSON object with:

                - visible (str): The sun visibility as a boolean value.
                - since (str): The start time of the current sun visibility interval.
                - until (str): The end time of the current sun visibility interval.
    """
    oaem = get_oaem(pos_x=pos_x, pos_y=pos_y, pos_z=pos_z, epsg=epsg)
    sun_track = SunTrack(pos_x=pos_x, pos_y=pos_y, pos_z=pos_z, epsg=epsg)
    sun_track.intersect_with_oaem(oaem)
    sun_az, sun_el = sun_track.current_sunpos
    sun_visible = sun_el > oaem.query(sun_az)

    return {
        "visible": str(sun_visible),
        "since": str(sun_track.since),
        "until": str(sun_track.until),
    }


@router.get("/plot", response_class=Response)
async def plot_oaem(pos_x: float, pos_y: float, epsg: int, pos_z: Optional[float] = None):
    """
    Computes the Obstruction Adaptive Elevation Mask (OAEM) for a given position and EPSG code, and returns a plot of the OAEM.

    Due to the unavailability of data for other federal states, the OAEM is currently only available for
    the state of North Rhine-Westphalia (NRW), Germany.

    Args:

        pos_x (float): The x-coordinate of the position.
        pos_y (float): The y-coordinate of the position.
        pos_z (float): The z-coordinate of the position.
        epsg (int): The EPSG code of the position.
        width (int, optional): The width of the plot in pixels. Defaults to 600.
        height (int, optional): The height of the plot in pixels. Defaults to 600.
        heading (float, optional): The heading of the plot in degrees. Defaults to 0.0.

    Returns:

        A JSON string representation of the Plotly figure.
    """
    oaem = get_oaem(pos_x=pos_x, pos_y=pos_y, pos_z=pos_z, epsg=epsg)
    sun_track = SunTrack(pos_x=pos_x, pos_y=pos_y, pos_z=pos_z, epsg=epsg)

    return create_json_fig(oaem, sun_track=sun_track)

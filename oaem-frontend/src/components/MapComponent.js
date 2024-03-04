import React, { useState, useMemo, useEffect } from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';
import LocationMarker from './LocationMarker';
import CurrentPositionButton from './CurrentPositionButton';

const initialPosition = [51, 6.89]
const initialZoom = 10

const MapComponent = ({ position, setPosition }) => {
    const [map, setMap] = useState(null)

    const displayMap = useMemo(
        () => (
            <MapContainer
                center={initialPosition}
                zoom={initialZoom}
                scrollWheelZoom={true}
                ref={setMap}>
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                <LocationMarker position={position} setPosition={setPosition} />
            </MapContainer>
        ),
        [position, setPosition],
    )

    useEffect(() => {
        if (map && position) {
            map.flyTo(position, Math.max(17, map.getZoom()));
        }
    }, [position, map])


    return (
        <div>
            {displayMap}
            {map ? <CurrentPositionButton setPosition={setPosition} /> : null}
        </div>
    )
};

export default MapComponent;

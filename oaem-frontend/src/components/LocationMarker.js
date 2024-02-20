import React from 'react';
import { Marker, Popup, useMapEvents } from 'react-leaflet';

const LocationMarker = ({ position, setPosition }) => {

    useMapEvents({
        click(e) {
            setPosition([
                e.latlng.lat,
                e.latlng.lng
            ]);
        },
    });

    const positionText = position === null ? 'null' : `Selected Position: ${position[0].toFixed(6)}°, ${position[1].toFixed(6)}°`;

    return position === null ? null : (
        <Marker position={position}>
            <Popup>{positionText}</Popup>
        </Marker>
    )
}

export default LocationMarker;
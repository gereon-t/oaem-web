import React from 'react';
import './CurrentPositionButton.css';

const CurrentPositionButton = ({ setPosition }) => {

    const setToCurrentPosition = () => {
        navigator.geolocation.getCurrentPosition((position) => {
            setPosition([position.coords.latitude, position.coords.longitude])
        }, console.error, { enableHighAccuracy: true, maximumAge: 0 })
    }

    return <button className='current-location-button' onClick={setToCurrentPosition}>Go To Current Location</button>
}

export default CurrentPositionButton;
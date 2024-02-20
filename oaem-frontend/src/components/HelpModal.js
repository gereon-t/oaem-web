import React from 'react';
import './HelpModal.css';
import example from '../example.png';

const HelpModal = ({ isOpen, setIsHelpModalOpen }) => {

    const onClose = () => {
        setIsHelpModalOpen(false);
    }

    return (
        isOpen && (
            <div className='modal'>
                <div className='help-modal-content'>
                    <div className='modal-title'>Help</div>

                    <div className='modal-container'>
                        <p>Click on any location <span className='bold-text'>within North Rhine-Westphalia, Germany,</span> to see the obstruction adaptive elevation mask (OAEM) for that location. </p>
                        <img className='example-image' src={example} alt='Example' />
                        <p>The plot that you will see is a so-called skyplot that depicts the view into the sky from a given position. The position of an object in this plot is described using azimuth (i.e. north 0°, east 90°, south 180°, west 270°) and elevation (0° horizon, 90° zenith). The grey area shows the blockage of the free sky view (blue) due to buildings. The yellow circle is the current position of the sun along its trajectory (black).</p>
                        <p>The darkblue outline of the sky view is called Obstruction Adaptive Elevation Mask (OAEM) [Zimmermann 2019]. It is possible to compute this OAEM from the user position because of existing CityGML databases. CityGML models are XML based representations of buildings and can either be retrieved from local file storage or from Web-Feature-Services (WFS). This data exists for most german or international cities, however, they are not always free.</p>
                        <p className='bold-text'>This website is designed for LOD1 building models from Geobasis NRW, Germany. In its current state, it is therefore only applicable within North Rhine-Westphalia, Germany.</p>
                    </div>
                    <div className='modal-button-group'>
                        <button className='modal-button' onClick={onClose}>Close</button>
                    </div>
                </div>
            </div >
        )
    );
};

export default HelpModal;
import React, { useEffect, useState } from 'react';
import './Modal.css'
import './PlotComponent.css'
import Plot from 'react-plotly.js';

const ENDPOINT_URL = 'api';

const getPlot = async (position) => {
    try {
        const response = await fetch(ENDPOINT_URL + '/plot?' + new URLSearchParams({
            pos_x: position[0],
            pos_y: position[1],
            epsg: 4326,
        }), {
            method: 'GET', headers: {
                'Content-Type': 'application/json',
            },
        });

        if (response.status !== 200) {
            throw new Error('Plotting failed');
        }

        try {
            const json_data = await response.json();
            return json_data;
        } catch (error) {
            console.error('Failed to parse response:', error);
        }

    } catch (error) {
        console.error('Failed to plot oaem:', error);
    }
};



const PlotModal = ({ isOpen, setIsPlotModalOpen, position }) => {
    const [loading, setLoading] = useState(false);
    const [plotlyFigure, setPlotlyFigure] = useState(null);

    useEffect(() => {
        if (position === null) return;

        setIsPlotModalOpen(true);
        setLoading(true);
        getPlot(position).then(response => setPlotlyFigure(response)).finally(() => setLoading(false));
    }, [position, setIsPlotModalOpen]);

    const onClose = () => {
        setIsPlotModalOpen(false);
    }

    return (
        position && isOpen && (
            <div className="modal">
                <div className="modal-content">
                    <div className='modal-title'>OAEM Plot</div>

                    <div className='modal-container'>
                        {loading ? <div className='loading-spinner' /> : <div className='modal-plot'>
                            {plotlyFigure ? <Plot
                                data={plotlyFigure.data}
                                layout={plotlyFigure.layout}
                            /> : "Failed to load plot"}
                        </div>}
                    </div>
                    <div className="modal-button-group">
                        <button className='modal-button' onClick={onClose}>Close</button>
                    </div>
                </div>
            </div>
        )
    );
};

export default PlotModal;
import React, { useState } from "react";

import './App.css';
import Header from "./components/Header";
import MapComponent from "./components/MapComponent";
import PlotModal from "./components/PlotComponent";
import Footer from "./components/Footer";


function App() {
  const [position, setPosition] = useState(null)
  const [isPlotModalOpen, setIsPlotModalOpen] = useState(false);


  return (
    <div>
      <Header />
      <PlotModal
        isOpen={isPlotModalOpen}
        setIsPlotModalOpen={setIsPlotModalOpen}
        position={position}
      />
      <div id="map">
        <MapComponent position={position} setPosition={setPosition} />
      </div>
      <Footer />
    </div>);
}

export default App;
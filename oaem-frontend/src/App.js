import React, { useState } from "react";

import './App.css';
import Header from "./components/Header";
import MapComponent from "./components/MapComponent";
import PlotModal from "./components/PlotComponent";
import Footer from "./components/Footer";
import HelpModal from "./components/HelpModal";


function App() {
  const [position, setPosition] = useState(null)
  const [isPlotModalOpen, setIsPlotModalOpen] = useState(false);
  const [isHelpModalOpen, setIsHelpModalOpen] = useState(false);


  return (
    <div>
      <Header />
      <PlotModal
        isOpen={isPlotModalOpen}
        setIsPlotModalOpen={setIsPlotModalOpen}
        position={position}
      />
      <HelpModal isOpen={isHelpModalOpen}
        setIsHelpModalOpen={setIsHelpModalOpen} />
      <div id="map">
        <MapComponent position={position} setPosition={setPosition} />
      </div>
      <Footer setIsHelpModalOpen={setIsHelpModalOpen} />
    </div>);
}

export default App;
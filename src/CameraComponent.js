import React from "react";
import Webcam from "react-webcam";
import "./CameraComponent.css";

const CameraComponent = () => {
    return (
        <div className="camera-container">
            <Webcam className="webcam" mirrored={false} />
        </div>
    );
};

export default CameraComponent
import './App.css';
import React, { useState } from 'react';
import CameraComponent from './CameraComponent.js';
import GestureAssignMenu from './GestureAssignMenu';

const App = () => {
  const [gestureKeyMap, setGestureKeyMap] = useState({});

  const handleGestureAssign = (gesture, keypress) => {
    setGestureKeyMap((prevMap) => ({...prevMap, [gesture]: keypress}));
  };

  return (
    <div className="App">
      <div className='taskbar'>
        <h1>Moveocado</h1>
        <GestureAssignMenu 
          gestureKeyMap={gestureKeyMap}
          onGestureAssign={handleGestureAssign}
          onDeleteGesture={(gesture) => {
            const updateKeyMap = {...gestureKeyMap};
            delete updateKeyMap[gesture];
            setGestureKeyMap(updateKeyMap);
          }}
        />
      </div>
      <CameraComponent />
    </div>
  );
}

export default App;

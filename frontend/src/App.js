import React, { useState } from 'react';
import axios from 'axios';
import Header from './components/Header';

function App() {
  const [videoFile, setVideoFile] = useState(null);
  const [videoDimensions, setVideoDimensions] = useState(null);

  const handleFileChange = (event) => {
    setVideoFile(event.target.files[0]);
  };

  const processVideo = async () => {
    if (!videoFile) {
      console.error("No video selected");
      return;
    }

    const formData = new FormData();
    formData.append('video', videoFile);

    try {
      const response = await axios.post('http://localhost:8000/api/process-video', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      setVideoDimensions(response.data.dimensions);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      <Header />
      <input type="file" accept="video/*" onChange={handleFileChange} />
      <button onClick={processVideo}>Process Video</button>
      {videoDimensions && (
        <div>
          <h2>Video Dimensions</h2>
          <p>{`Width: ${videoDimensions.width}, Height: ${videoDimensions.height}`}</p>
        </div>
      )}
    </div>
  );
}

export default App;


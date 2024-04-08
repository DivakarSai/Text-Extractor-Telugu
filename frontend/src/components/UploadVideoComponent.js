import React, { useState } from 'react';
import axios from 'axios';

const UploadVideoComponent = ({ setProcessedData }) => {
  const [videoFile, setVideoFile] = useState(null);
  const [language, setLanguage] = useState('');
  const [x, setX] = useState('');
  const [y, setY] = useState('');
  const [w, setW] = useState('');
  const [h, setH] = useState('');

  const handleFileChange = (event) => {
    setVideoFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('video', videoFile);
    formData.append('language', language);
    formData.append('x', x);
    formData.append('y', y);
    formData.append('w', w);
    formData.append('h', h);

    try {
      const response = await axios.post('http://localhost:8000/api/process-video', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setProcessedData(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Upload Video</h2>
      <input type="file" accept="video/*" onChange={handleFileChange} />
      <div>
        <label>Language:</label>
        <input type="text" value={language} onChange={(e) => setLanguage(e.target.value)} />
      </div>
      <div>
        <label>X:</label>
        <input type="text" value={x} onChange={(e) => setX(e.target.value)} />
      </div>
      <div>
        <label>Y:</label>
        <input type="text" value={y} onChange={(e) => setY(e.target.value)} />
      </div>
      <div>
        <label>Width:</label>
        <input type="text" value={w} onChange={(e) => setW(e.target.value)} />
      </div>
      <div>
        <label>Height:</label>
        <input type="text" value={h} onChange={(e) => setH(e.target.value)} />
      </div>
      <button onClick={handleUpload}>Upload Video</button>
    </div>
  );
};

export default UploadVideoComponent;

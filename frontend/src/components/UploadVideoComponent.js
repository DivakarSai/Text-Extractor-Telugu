import React, { useState } from 'react';
import axios from 'axios';
import {Input} from "@nextui-org/react";

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
      <div className="flex w-full flex-wrap md:flex-nowrap gap-4">
      <Input type="text" label="Language" placeholder="Language of the text" />
      </div>
      <div className="flex w-full flex-wrap md:flex-nowrap gap-4">
      <Input type="text" label="X" placeholder="Top of region of interest" />
      </div>
      <div className="flex w-full flex-wrap md:flex-nowrap gap-4">
      <Input type="text" label="Y" placeholder="left of region of interest" />
      </div>
      <div className="flex w-full flex-wrap md:flex-nowrap gap-4">
      <Input type="text" label="Width" placeholder="Width of region of interest" />
      </div>
      <div className="flex w-full flex-wrap md:flex-nowrap gap-4">
      <Input type="text" label="Height" placeholder="Height of region of interest" />
      </div>
      <button onClick={handleUpload}>Upload Video</button>
    </div>
  );
};

export default UploadVideoComponent;

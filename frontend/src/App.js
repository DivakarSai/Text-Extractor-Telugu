import React, { useState } from 'react';
import UploadVideoComponent from './components/UploadVideoComponent';
import DisplayImageWithBoundingBox from './components/DisplayImageWithBoundingBox';
import Header from './components/Header';

function App() {
  const [processedData, setProcessedData] = useState(null);

  return (
    <div className="App">
      <Header />
      <UploadVideoComponent setProcessedData={setProcessedData} />
      {processedData && <DisplayImageWithBoundingBox processedData={processedData} />}
      {processedData && (
        <div>
          <h2>Extracted Text</h2>
          <p>{processedData.extracted_text}</p>
        </div>
      )}
    </div>
  );
}

export default App;

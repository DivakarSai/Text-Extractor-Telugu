import React from 'react';

const DisplayImageWithBoundingBox = ({ processedData }) => {
  const { image_with_bounding_box } = processedData;

  return (
    <div>
      <h2>Image with Bounding Box</h2>
      <img src={image_with_bounding_box} alt="Image with Bounding Box" />
    </div>
  );
};

export default DisplayImageWithBoundingBox;

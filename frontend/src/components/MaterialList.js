import React from 'react';

function MaterialList({ materials }) {
  return (
    <div>
      <h2>Materials List</h2>
      <ul>
        {materials.map((material) => (
          <li key={material.id}>
            <strong>{material.material_name}</strong> (HS Code: {material.hs_code})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MaterialList;

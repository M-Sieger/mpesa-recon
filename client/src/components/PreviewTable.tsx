import React from "react";

interface PreviewTableProps {
  csvData: Record<string, string>[];
}

const PreviewTable: React.FC<PreviewTableProps> = ({ csvData }) => (
  <div className="preview-section">
    <h3>📋 Datenvorschau</h3>
    <div className="table-container">
      <table className="upload-table">
        <thead>
          <tr>
            {Object.keys(csvData[0]).map((header, idx) => (
              <th key={idx}>{header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {csvData.slice(0, 5).map((row, idx) => (
            <tr key={idx}>
              {Object.values(row).map((cell, i) => (
                <td key={i}>{cell}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      {csvData.length > 5 && (
        <p className="preview-note">... und {csvData.length - 5} weitere Zeilen</p>
      )}
    </div>
  </div>
);

export default PreviewTable;

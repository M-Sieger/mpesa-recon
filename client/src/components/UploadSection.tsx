import React from "react";

interface UploadSectionProps {
  handleFileUpload: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const UploadSection: React.FC<UploadSectionProps> = ({ handleFileUpload }) => (
  <div className="upload-area">
    <div className="upload-intro">
      <h2>📂 M-PESA Daten Upload</h2>
      <p className="upload-help">
        📋 Dieses Tool hilft dir bei deiner Buchhaltung – kostenlos & anonym
      </p>
      <p className="upload-formats">
        Unterstützte Formate: CSV, XLSX, PDF (PDF wird automatisch erkannt)
      </p>
    </div>
    <input
      type="file"
      accept=".csv,.xlsx,.xls,.pdf"
      onChange={handleFileUpload}
      className="upload-input"
      id="file-upload"
    />
    <label htmlFor="file-upload" className="upload-label">
      📁 Datei auswählen oder hier ablegen
    </label>
  </div>
);

export default UploadSection;

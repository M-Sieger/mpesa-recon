import React from "react";

interface FileInfoProps {
  fileName: string;
  fileSize: number;
  rowCount: number;
  isProcessing: boolean;
  formatFileSize: (bytes: number) => string;
}

const FileInfo: React.FC<FileInfoProps> = ({
  fileName,
  fileSize,
  rowCount,
  isProcessing,
  formatFileSize,
}) => (
  <div className="file-info">
    <div className="file-details">
      <p>
        ✅ Datei geladen: <strong>{fileName}</strong>
      </p>
      <p className="file-meta">
        Größe: {formatFileSize(fileSize)}
        {rowCount > 0 && ` • ${rowCount} Zeilen erkannt`}
      </p>
      {isProcessing && (
        <p className="processing-status">
          🔄 {fileName.toLowerCase().endsWith(".pdf")
            ? "PDF wird verarbeitet..."
            : "Datei wird verarbeitet..."}
        </p>
      )}
    </div>
  </div>
);

export default FileInfo;

import React, { useState } from "react";
import Papa from "papaparse";
import UploadSection from "./UploadSection";
import FileInfo from "./FileInfo";
import AnalyzeButton from "./AnalyzeButton";
import PreviewTable from "./PreviewTable";
import { parsePDFToCSV } from "../utils/pdfParser";

type CSVRow = Record<string, string>;

const UploadAndPreview: React.FC = () => {
  const [csvData, setCsvData] = useState<CSVRow[]>([]);
  const [fileName, setFileName] = useState<string>("");
  const [fileSize, setFileSize] = useState<number>(0);
  const [isAnalyzing, setIsAnalyzing] = useState<boolean>(false);
  const [isProcessing, setIsProcessing] = useState<boolean>(false);
  const [showPasswordInput, setShowPasswordInput] = useState<boolean>(false);
  const [password, setPassword] = useState<string>("");
  const [currentFile, setCurrentFile] = useState<File | null>(null);
  const [passwordError, setPasswordError] = useState<string>("");

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setFileName(file.name);
    setFileSize(file.size);
    setCurrentFile(file);
    setIsProcessing(true);
    setShowPasswordInput(false);
    setPasswordError("");

    await processFile(file);
  };

  const processFile = async (file: File, pdfPassword: string | null = null) => {
    try {
      if (file.name.toLowerCase().endsWith(".csv")) {
        Papa.parse<CSVRow>(file, {
          header: true,
          skipEmptyLines: true,
          complete: function (results) {
            setCsvData(results.data);
            setIsProcessing(false);
          },
        });
      } else if (file.name.toLowerCase().endsWith(".pdf")) {
        try {
          const transactions = await parsePDFToCSV(file, pdfPassword);
          setCsvData(transactions);
          setIsProcessing(false);
          setShowPasswordInput(false);
        } catch (error: any) {
          if (error.message === "PASSWORD_REQUIRED") {
            setIsProcessing(false);
            setShowPasswordInput(true);
            setPasswordError("Diese PDF-Datei ist passwortgeschützt. Bitte geben Sie das Passwort ein.");
          } else if (error.message === "INVALID_PASSWORD") {
            setPasswordError("Falsches Passwort. Bitte versuchen Sie es erneut.");
          } else {
            setIsProcessing(false);
            alert("Fehler beim Verarbeiten der PDF-Datei: " + error.message);
          }
        }
      } else if (file.name.toLowerCase().endsWith(".xlsx") || file.name.toLowerCase().endsWith(".xls")) {
        setCsvData([]);
        setIsProcessing(false);
        alert("Excel-Verarbeitung kommt bald!");
      }
    } catch (error) {
      console.error("File processing error:", error);
      setIsProcessing(false);
      alert("Fehler beim Verarbeiten der Datei");
    }
  };

  const handlePasswordSubmit = async () => {
    if (!password.trim()) {
      setPasswordError("Bitte geben Sie ein Passwort ein.");
      return;
    }

    setIsProcessing(true);
    setPasswordError("");

    if (currentFile) {
      await processFile(currentFile, password);
    }
  };

  const handlePasswordCancel = () => {
    setShowPasswordInput(false);
    setPassword("");
    setPasswordError("");
    setCurrentFile(null);
    setFileName("");
    setFileSize(0);
  };

  const handleAnalyze = () => {
    setIsAnalyzing(true);
    setTimeout(() => {
      setIsAnalyzing(false);
      alert("Analyse abgeschlossen! (Demo-Funktion)");
    }, 2000);
  };

  const formatFileSize = (bytes: number): string => {
    if (bytes === 0) return "0 Bytes";
    const k = 1024;
    const sizes = ["Bytes", "KB", "MB", "GB"];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i];
  };

  return (
    <div className="upload-wrapper">
      <UploadSection handleFileUpload={handleFileUpload} />
      {fileName && (
        <>
          <FileInfo
            fileName={fileName}
            fileSize={fileSize}
            rowCount={csvData.length}
            isProcessing={isProcessing}
            formatFileSize={formatFileSize}
          />
          {csvData.length > 0 && !isProcessing && !showPasswordInput && (
            <AnalyzeButton isAnalyzing={isAnalyzing} onAnalyze={handleAnalyze} />
          )}
        </>
      )}

      {csvData.length > 0 && <PreviewTable csvData={csvData} />}

      {showPasswordInput && (
        <div className="password-input-section">
          <div className="password-input-container">
            <h3>🔒 PDF Passwort erforderlich</h3>
            <p className="password-help">
              Diese M-PESA PDF-Datei ist passwortgeschützt. Geben Sie das Passwort ein, um fortzufahren.
            </p>
            {passwordError && <p className="password-error">{passwordError}</p>}
            <div className="password-input-group">
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="PDF Passwort eingeben..."
                className="password-input"
                onKeyPress={(e) => e.key === "Enter" && handlePasswordSubmit()}
              />
              <div className="password-buttons">
                <button className="password-submit-button" onClick={handlePasswordSubmit} disabled={isProcessing}>
                  {isProcessing ? "🔄 Verarbeite..." : "🔓 PDF öffnen"}
                </button>
                <button className="password-cancel-button" onClick={handlePasswordCancel} disabled={isProcessing}>
                  ❌ Abbrechen
                </button>
              </div>
            </div>
            <p className="password-hint">
              💡 <strong>Tipp:</strong> Das Passwort ist oft Ihre Telefonnummer oder ein von Safaricom bereitgestelltes Passwort.
            </p>
          </div>
        </div>
      )}
    </div>
  );
};

export default UploadAndPreview;

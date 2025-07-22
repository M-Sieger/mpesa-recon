import React from "react";

interface AnalyzeButtonProps {
  isAnalyzing: boolean;
  onAnalyze: () => void;
}

const AnalyzeButton: React.FC<AnalyzeButtonProps> = ({ isAnalyzing, onAnalyze }) => (
  <button className="analyze-button" onClick={onAnalyze} disabled={isAnalyzing}>
    {isAnalyzing ? "🔄 Analysiere..." : "📊 Jetzt analysieren"}
  </button>
);

export default AnalyzeButton;

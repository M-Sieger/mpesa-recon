import './App.css';

import { useState } from 'react';

import { useTranslation } from 'react-i18next';

import { LanguageSwitcher } from './components/LanguageSwitcher';
import type { MemberFormData } from './components/MemberForm';
import { MemberForm } from './components/MemberForm';
import type { ProgressStage } from './components/ProgressIndicator';
import { ProgressIndicator } from './components/ProgressIndicator';
import { ReportPreview } from './components/ReportPreview';
import { UploadZone } from './components/UploadZone';
import { useGenerateReport } from './hooks/useGenerateReport';

type AppStage = 'upload' | 'form' | 'processing' | 'preview';

function App() {
  const { t } = useTranslation();
  
  const [stage, setStage] = useState<AppStage>('upload');
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [progressStage, setProgressStage] = useState<ProgressStage>('parsing');
  const [reportData, setReportData] = useState<{
    url: string;
    verificationCode: string;
    filename: string;
  } | null>(null);

  const { mutate: generateReport, isPending, error } = useGenerateReport({
    onProgress: (stage) => {
      setProgressStage(stage as ProgressStage);
    },
    onSuccess: (data) => {
      setReportData({
        url: data.reportUrl,
        verificationCode: data.verificationCode,
        filename: data.filename,
      });
      setStage('preview');
    },
  });

  const handleFileSelect = (file: File) => {
    setSelectedFile(file);
    setStage('form');
  };

  const handleFormSubmit = (data: MemberFormData) => {
    if (!selectedFile) return;

    setStage('processing');
    setProgressStage('parsing');

    generateReport({
      file: selectedFile,
      memberName: data.memberName,
      mobile: data.mobile,
      email: data.email,
      password: data.password,
      notes: data.notes,
    });
  };

  const handleDownload = async () => {
    if (!reportData) return;

    try {
      const response = await fetch(reportData.url);
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = reportData.filename;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    } catch (err) {
      console.error('Download failed:', err);
    }
  };

  const handleReset = () => {
    setStage('upload');
    setSelectedFile(null);
    setReportData(null);
    setProgressStage('parsing');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 via-white to-secondary-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
          <div>
            <h1 className="text-2xl font-bold text-primary-700">{t('app.title')}</h1>
            <p className="text-sm text-gray-600 mt-1">{t('app.tagline')}</p>
          </div>
          <LanguageSwitcher />
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {stage === 'upload' && (
          <div className="max-w-2xl mx-auto">
            <div className="text-center mb-8">
              <h2 className="text-3xl font-bold text-gray-900 mb-2">{t('upload.title')}</h2>
              <p className="text-gray-600">{t('upload.subtitle')}</p>
            </div>
            <UploadZone onFileSelect={handleFileSelect} selectedFile={selectedFile} />
          </div>
        )}

        {stage === 'form' && selectedFile && (
          <div className="max-w-2xl mx-auto">
            <div className="bg-white rounded-lg shadow-md p-8">
              <div className="mb-6">
                <h2 className="text-2xl font-bold text-gray-900 mb-2">{t('upload.title')}</h2>
                <p className="text-sm text-gray-600">
                  {t('upload.fileSelected')} <span className="font-medium">{selectedFile.name}</span>
                </p>
              </div>
              <MemberForm onSubmit={handleFormSubmit} isLoading={isPending} />
              {error && (
                <div className="mt-4 p-4 bg-error-50 border border-error-200 rounded-lg">
                  <p className="text-sm text-error-700">{error.message}</p>
                </div>
              )}
            </div>
          </div>
        )}

        {stage === 'processing' && (
          <div className="max-w-4xl mx-auto">
            <ProgressIndicator currentStage={progressStage} />
          </div>
        )}

        {stage === 'preview' && reportData && (
          <div>
            <ReportPreview
              pdfUrl={reportData.url}
              verificationCode={reportData.verificationCode}
              onDownload={handleDownload}
            />
            <div className="max-w-5xl mx-auto mt-6 text-center">
              <button
                onClick={handleReset}
                className="bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium 
                         px-6 py-3 rounded-lg transition-colors border border-gray-300"
              >
                {t('button.tryAnother')}
              </button>
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="text-center">
            <p className="text-sm text-gray-600">{t('footer.poweredBy')}</p>
            <p className="text-xs text-gray-500 mt-2">{t('footer.helpText')}</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;

import {
  CheckCircle,
  Download,
  ExternalLink,
} from 'lucide-react';
import { useTranslation } from 'react-i18next';

interface ReportPreviewProps {
  pdfUrl: string;
  verificationCode: string;
  onDownload: () => void;
}

export function ReportPreview({ pdfUrl, verificationCode, onDownload }: ReportPreviewProps) {
  const { t } = useTranslation();

  return (
    <div className="w-full max-w-5xl mx-auto space-y-6">
      {/* Success Message */}
      <div className="bg-success-50 border border-success-200 rounded-lg p-6">
        <div className="flex items-center gap-3">
          <CheckCircle className="h-8 w-8 text-success-600 flex-shrink-0" />
          <div className="flex-1">
            <h3 className="text-lg font-semibold text-success-900">{t('success.title')}</h3>
            <p className="text-sm text-success-700 mt-1">{t('success.message')}</p>
          </div>
        </div>

        {/* Verification Code */}
        <div className="mt-4 bg-white rounded-lg p-4 border border-success-300">
          <p className="text-sm font-medium text-gray-700 mb-2">{t('success.verificationCode')}</p>
          <p className="text-2xl font-mono font-bold text-primary-700 tracking-wider">
            {verificationCode}
          </p>
          <p className="text-xs text-gray-600 mt-2">{t('success.verificationInstructions')}</p>
        </div>
      </div>

      {/* PDF Preview */}
      <div className="bg-white rounded-lg shadow-lg border border-gray-200 overflow-hidden">
        <div className="bg-gray-50 border-b border-gray-200 px-6 py-4 flex items-center justify-between">
          <h3 className="text-lg font-semibold text-gray-900">{t('preview.title')}</h3>
          
          {/* Action Buttons */}
          <div className="flex gap-3">
            <button
              onClick={onDownload}
              className="flex items-center gap-2 bg-primary-600 hover:bg-primary-700 
                       text-white font-medium px-4 py-2 rounded-lg transition-colors 
                       shadow-sm hover:shadow-md"
            >
              <Download className="h-5 w-5" />
              {t('button.download')}
            </button>
            
            <a
              href={pdfUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-2 bg-gray-100 hover:bg-gray-200 
                       text-gray-700 font-medium px-4 py-2 rounded-lg transition-colors
                       border border-gray-300"
            >
              <ExternalLink className="h-5 w-5" />
              {t('button.openNew')}
            </a>
          </div>
        </div>

        {/* PDF Embed */}
        <div className="w-full h-[800px]">
          <iframe
            src={pdfUrl}
            className="w-full h-full"
            title={t('preview.title')}
          />
        </div>
      </div>

      {/* Instructions */}
      <div className="bg-blue-50 border border-blue-200 rounded-lg p-6">
        <h4 className="text-md font-semibold text-blue-900 mb-3">{t('preview.nextSteps')}</h4>
        <ul className="space-y-2 text-sm text-blue-800">
          <li className="flex items-start gap-2">
            <span className="text-blue-600 mt-0.5">•</span>
            <span>{t('preview.step1')}</span>
          </li>
          <li className="flex items-start gap-2">
            <span className="text-blue-600 mt-0.5">•</span>
            <span>{t('preview.step2')}</span>
          </li>
          <li className="flex items-start gap-2">
            <span className="text-blue-600 mt-0.5">•</span>
            <span>{t('preview.step3')}</span>
          </li>
        </ul>
      </div>
    </div>
  );
}

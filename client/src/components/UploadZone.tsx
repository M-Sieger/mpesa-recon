import { useCallback } from 'react';

import {
  AlertCircle,
  FileText,
  Upload,
} from 'lucide-react';
import { useDropzone } from 'react-dropzone';
import { useTranslation } from 'react-i18next';

interface UploadZoneProps {
  onFileSelect: (file: File) => void;
  selectedFile: File | null;
  error?: string;
}

const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB

export function UploadZone({ onFileSelect, selectedFile, error }: UploadZoneProps) {
  const { t } = useTranslation();

  const onDrop = useCallback(
    (acceptedFiles: File[], rejectedFiles: any[]) => {
      if (rejectedFiles.length > 0) {
        const rejection = rejectedFiles[0];
        if (rejection.errors[0]?.code === 'file-too-large') {
          // Error will be handled by parent component
          return;
        }
        if (rejection.errors[0]?.code === 'file-invalid-type') {
          // Error will be handled by parent component
          return;
        }
      }

      if (acceptedFiles.length > 0) {
        const file = acceptedFiles[0];
        if (file.size > MAX_FILE_SIZE) {
          // Parent will handle error
          return;
        }
        onFileSelect(file);
      }
    },
    [onFileSelect]
  );

  const { getRootProps, getInputProps, isDragActive, isDragReject } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': ['.pdf'],
    },
    maxSize: MAX_FILE_SIZE,
    multiple: false,
  });

  return (
    <div className="w-full">
      <div
        {...getRootProps()}
        className={`
          relative border-2 border-dashed rounded-card p-12 
          transition-all duration-200 cursor-pointer
          ${
            isDragActive && !isDragReject
              ? 'border-primary-500 bg-primary-50'
              : isDragReject
              ? 'border-error-500 bg-error-50'
              : selectedFile
              ? 'border-success-500 bg-success-50'
              : 'border-gray-300 bg-gray-50 hover:border-primary-400 hover:bg-primary-25'
          }
        `}
      >
        <input {...getInputProps()} />

        <div className="flex flex-col items-center justify-center text-center space-y-4">
          {/* Icon */}
          <div
            className={`
            w-16 h-16 rounded-full flex items-center justify-center
            ${
              isDragActive && !isDragReject
                ? 'bg-primary-100'
                : isDragReject
                ? 'bg-error-100'
                : selectedFile
                ? 'bg-success-100'
                : 'bg-gray-100'
            }
          `}
          >
            {selectedFile ? (
              <FileText
                className={`w-8 h-8 ${isDragReject ? 'text-error-600' : 'text-success-600'}`}
              />
            ) : (
              <Upload
                className={`w-8 h-8 ${
                  isDragActive && !isDragReject
                    ? 'text-primary-600'
                    : isDragReject
                    ? 'text-error-600'
                    : 'text-gray-600'
                }`}
              />
            )}
          </div>

          {/* Text */}
          <div>
            {selectedFile ? (
              <>
                <p className="text-lg font-medium text-success-700">{t('upload.fileSelected')}</p>
                <p className="text-sm text-gray-600 mt-1">{selectedFile.name}</p>
                <p className="text-xs text-gray-500 mt-1">
                  {(selectedFile.size / 1024 / 1024).toFixed(2)} MB
                </p>
              </>
            ) : (
              <>
                <p className="text-lg font-medium text-gray-700">
                  {isDragActive && !isDragReject
                    ? t('upload.dragactive')
                    : t('upload.dragdrop')}
                </p>
                <p className="text-sm text-gray-500 mt-2">{t('upload.maxSize')}</p>
                <p className="text-xs text-gray-400 mt-1">{t('upload.acceptedFormat')}</p>
              </>
            )}
          </div>
        </div>
      </div>

      {/* Error Message */}
      {error && (
        <div className="mt-4 p-4 bg-error-50 border border-error-200 rounded-lg flex items-start gap-3">
          <AlertCircle className="w-5 h-5 text-error-600 flex-shrink-0 mt-0.5" />
          <div>
            <p className="text-sm font-medium text-error-800">{error}</p>
          </div>
        </div>
      )}
    </div>
  );
}

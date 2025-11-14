import axios, { AxiosError } from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export interface GenerateReportRequest {
  file: File;
  memberName: string;
  mobile: string;
  email?: string;
  password?: string;
  notes?: string;
}

export interface GenerateReportResponse {
  reportUrl: string;
  verificationCode: string;
  filename: string;
}

export interface ApiError {
  detail: string;
  code?: string;
}

class ReportApiError extends Error {
  public message: string;
  public code?: string;
  public status?: number;

  constructor(message: string, code?: string, status?: number) {
    super(message);
    this.message = message;
    this.code = code;
    this.status = status;
    this.name = 'ReportApiError';
  }
}

/**
 * Generate a loan-ready report from an M-Pesa PDF statement
 */
export async function generateReport(
  request: GenerateReportRequest,
  onProgress?: (stage: string) => void
): Promise<GenerateReportResponse> {
  const formData = new FormData();
  formData.append('file', request.file);
  formData.append('member_name', request.memberName);
  formData.append('mobile', request.mobile);
  
  if (request.email) {
    formData.append('email', request.email);
  }
  
  if (request.password) {
    formData.append('password', request.password);
  }
  
  if (request.notes) {
    formData.append('notes', request.notes);
  }

  try {
    // Simulate progress updates (since backend doesn't stream progress yet)
    if (onProgress) {
      onProgress('parsing');
      setTimeout(() => onProgress('categorizing'), 1000);
      setTimeout(() => onProgress('summarizing'), 2000);
      setTimeout(() => onProgress('generating'), 3000);
    }

    const response = await axios.post<Blob>(
      `${API_BASE_URL}/api/v1/report/generate`,
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        responseType: 'blob',
        timeout: 60000, // 60 second timeout
      }
    );

    // Extract verification code from response headers
    const verificationCode = response.headers['x-verification-code'] || 'UNKNOWN';
    const filename = response.headers['content-disposition']
      ?.split('filename=')[1]
      ?.replace(/"/g, '') || 'report.pdf';

    // Create blob URL for preview
    const blob = new Blob([response.data], { type: 'application/pdf' });
    const reportUrl = URL.createObjectURL(blob);

    if (onProgress) {
      onProgress('complete');
    }

    return {
      reportUrl,
      verificationCode,
      filename,
    };
  } catch (error) {
    if (axios.isAxiosError(error)) {
      const axiosError = error as AxiosError<ApiError>;
      
      if (axiosError.response) {
        // Server responded with error
        const status = axiosError.response.status;
        const detail = axiosError.response.data?.detail || 'Unknown error occurred';
        const code = axiosError.response.data?.code;

        if (status === 422) {
          throw new ReportApiError('Invalid file or parameters', code, status);
        } else if (status === 500) {
          throw new ReportApiError('Server error. Please try again.', code, status);
        } else {
          throw new ReportApiError(detail, code, status);
        }
      } else if (axiosError.request) {
        // Request made but no response
        throw new ReportApiError('Network error. Please check your connection.', 'NETWORK_ERROR');
      } else {
        // Error setting up request
        throw new ReportApiError(axiosError.message, 'REQUEST_ERROR');
      }
    }

    // Unknown error type
    throw new ReportApiError('An unexpected error occurred', 'UNKNOWN_ERROR');
  }
}

/**
 * Download the generated report
 */
export function downloadReport(blob: Blob, filename: string): void {
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
}

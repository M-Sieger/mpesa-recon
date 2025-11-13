import { useMutation } from '@tanstack/react-query';

import type {
  GenerateReportRequest,
  GenerateReportResponse,
} from '../api/reportApi';
import { generateReport } from '../api/reportApi';

interface UseGenerateReportOptions {
  onProgress?: (stage: string) => void;
  onSuccess?: (data: GenerateReportResponse) => void;
  onError?: (error: Error) => void;
}

export function useGenerateReport(options?: UseGenerateReportOptions) {
  return useMutation<GenerateReportResponse, Error, GenerateReportRequest>({
    mutationFn: (request) => generateReport(request, options?.onProgress),
    onSuccess: options?.onSuccess,
    onError: options?.onError,
  });
}

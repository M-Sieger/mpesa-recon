import {
  CheckCircle,
  FileBarChart,
  FilePlus,
  FileText,
  Loader2,
  Tags,
} from 'lucide-react';
import { useTranslation } from 'react-i18next';

export type ProgressStage = 'parsing' | 'categorizing' | 'summarizing' | 'generating' | 'complete';

interface ProgressIndicatorProps {
  currentStage: ProgressStage;
}

interface Stage {
  id: ProgressStage;
  icon: React.ElementType;
  labelKey: string;
}

const stages: Stage[] = [
  { id: 'parsing', icon: FileText, labelKey: 'progress.parsing' },
  { id: 'categorizing', icon: Tags, labelKey: 'progress.categorizing' },
  { id: 'summarizing', icon: FileBarChart, labelKey: 'progress.summarizing' },
  { id: 'generating', icon: FilePlus, labelKey: 'progress.generating' },
  { id: 'complete', icon: CheckCircle, labelKey: 'progress.complete' },
];

export function ProgressIndicator({ currentStage }: ProgressIndicatorProps) {
  const { t } = useTranslation();

  const currentIndex = stages.findIndex((s) => s.id === currentStage);

  return (
    <div className="w-full max-w-3xl mx-auto py-8">
      {/* Progress Bar Container */}
      <div className="relative">
        {/* Background Line */}
        <div className="absolute top-5 left-0 w-full h-1 bg-gray-200"></div>
        
        {/* Active Progress Line */}
        <div
          className="absolute top-5 left-0 h-1 bg-primary-600 transition-all duration-500"
          style={{ width: `${(currentIndex / (stages.length - 1)) * 100}%` }}
        ></div>

        {/* Stages */}
        <div className="relative flex justify-between">
          {stages.map((stage, index) => {
            const isActive = index === currentIndex;
            const isComplete = index < currentIndex;
            const isPending = index > currentIndex;

            const Icon = stage.icon;

            return (
              <div key={stage.id} className="flex flex-col items-center">
                {/* Icon Container */}
                <div
                  className={`
                    relative z-10 flex items-center justify-center w-12 h-12 rounded-full 
                    transition-all duration-300 shadow-lg
                    ${isComplete ? 'bg-success-500 text-white' : ''}
                    ${isActive ? 'bg-primary-600 text-white animate-pulse' : ''}
                    ${isPending ? 'bg-white border-2 border-gray-300 text-gray-400' : ''}
                  `}
                >
                  {isActive ? (
                    <Loader2 className="h-6 w-6 animate-spin" />
                  ) : (
                    <Icon className="h-6 w-6" />
                  )}
                </div>

                {/* Label */}
                <p
                  className={`
                    mt-3 text-sm font-medium text-center max-w-[80px]
                    ${isActive ? 'text-primary-700' : ''}
                    ${isComplete ? 'text-success-700' : ''}
                    ${isPending ? 'text-gray-500' : ''}
                  `}
                >
                  {t(stage.labelKey)}
                </p>
              </div>
            );
          })}
        </div>
      </div>

      {/* Current Stage Message */}
      <div className="mt-8 text-center">
        <p className="text-lg font-medium text-gray-800">
          {t(`progress.${currentStage}Message`)}
        </p>
      </div>
    </div>
  );
}

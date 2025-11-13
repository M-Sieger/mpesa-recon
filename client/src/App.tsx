import './index.css';

import { useTranslation } from 'react-i18next';

import {
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query';

import { LanguageSwitcher } from './components/LanguageSwitcher';
import UploadAndPreview from './components/UploadAndPreview';

const queryClient = new QueryClient();

function App() {
  const { t } = useTranslation();

  return (
    <QueryClientProvider client={queryClient}>
      <div className="min-h-screen bg-gradient-to-br from-primary-50 via-white to-secondary-50">
        {/* Header */}
        <header className="bg-white border-b border-gray-200 shadow-sm">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <div className="flex items-center justify-between">
              <div>
                <h1 className="text-2xl font-bold font-heading text-primary-600">
                  {t('app.title')}
                </h1>
                <p className="text-sm text-gray-600 mt-1">{t('app.tagline')}</p>
              </div>
              <LanguageSwitcher />
            </div>
          </div>
        </header>

        {/* Main Content */}
        <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <UploadAndPreview />
        </main>

        {/* Footer */}
        <footer className="bg-white border-t border-gray-200 mt-16">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div className="text-center text-sm text-gray-600">
              <p>{t('footer.poweredBy')}</p>
              <p className="mt-2 text-gray-500">{t('footer.helpText')}</p>
            </div>
          </div>
        </footer>
      </div>
    </QueryClientProvider>
  );
}

export default App;

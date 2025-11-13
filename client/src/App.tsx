/**
 * App.tsx – Main Application Component
 *
 * Purpose: Root component that provides app-wide layout and context providers
 * Why: Centralized place for global state management and consistent UI structure
 *
 * Architecture:
 * 1. QueryClientProvider: Manages server state (API calls, caching)
 * 2. i18n: Multi-language support (Swahili/English)
 * 3. Layout: Header → Main Content → Footer
 *
 * Design Pattern: Container/Presentational
 * - This is a presentational component (UI structure)
 * - Business logic lives in child components (UploadAndPreview, etc.)
 */

import './index.css';

// i18n hook for translations (Swahili/English)
import { useTranslation } from 'react-i18next';

// TanStack Query for server state management (API calls, caching, auto-retry)
// Why: Better than useState + useEffect for API data (automatic caching, refetching, error handling)
import {
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query';

// Components
import { LanguageSwitcher } from './components/LanguageSwitcher';
import UploadAndPreview from './components/UploadAndPreview';

/**
 * QueryClient Configuration
 * Why: Global settings for all API calls in the app
 *
 * Options:
 * - defaultOptions: Apply to all queries/mutations unless overridden
 */
const queryClient = new QueryClient();

function App() {
  // Hook: Get translation function
  // t('key') returns translated text based on current language
  const { t } = useTranslation();

  return (
    /**
     * QueryClientProvider: Makes queryClient available to all child components
     * Why: Any component can use useQuery/useMutation hooks for API calls
     */
    <QueryClientProvider client={queryClient}>
      {/*
        Root Container: Full-height gradient background
        - min-h-screen: Ensures content fills viewport height
        - bg-gradient: Subtle teal→white→green gradient (SACCO-friendly colors)
      */}
      <div className="min-h-screen bg-gradient-to-br from-primary-50 via-white to-secondary-50">

        {/* ========================================
            HEADER: Branding + Language Switcher
            ======================================== */}
        <header className="bg-white border-b border-gray-200 shadow-sm">
          {/* Container: Max-width with responsive padding */}
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            {/* Flexbox: Logo left, Language switcher right */}
            <div className="flex items-center justify-between">

              {/* Brand Section */}
              <div>
                {/*
                  Title: M-Recon (from translation file)
                  font-heading: Poppins font (bold, attention-grabbing)
                  text-primary-600: Teal color (trust, growth)
                */}
                <h1 className="text-2xl font-bold font-heading text-primary-600">
                  {t('app.title')}
                </h1>
                {/* Tagline: "Strengthen your loan applications" */}
                <p className="text-sm text-gray-600 mt-1">{t('app.tagline')}</p>
              </div>

              {/* Language Toggle: EN ⇄ SW */}
              <LanguageSwitcher />
            </div>
          </div>
        </header>

        {/* ========================================
            MAIN CONTENT: Upload Workflow
            ======================================== */}
        {/*
          Main container:
          - max-w-5xl: Optimal reading width (prevents overly wide content)
          - mx-auto: Center horizontally
          - py-12: Vertical spacing (top/bottom)
        */}
        <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          {/*
            Core Feature: PDF Upload → Member Form → Report Generation
            This component handles the entire user flow
          */}
          <UploadAndPreview />
        </main>

        {/* ========================================
            FOOTER: Credits + Help Text
            ======================================== */}
        <footer className="bg-white border-t border-gray-200 mt-16">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div className="text-center text-sm text-gray-600">
              {/* "Powered by M-Recon" */}
              <p>{t('footer.poweredBy')}</p>
              {/* Help text (e.g., "Need help? Contact support") */}
              <p className="mt-2 text-gray-500">{t('footer.helpText')}</p>
            </div>
          </div>
        </footer>
      </div>
    </QueryClientProvider>
  );
}

export default App;

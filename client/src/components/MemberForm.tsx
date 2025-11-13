import {
  FileText,
  Lock,
  Mail,
  Phone,
  User,
} from 'lucide-react';
import { useForm } from 'react-hook-form';
import { useTranslation } from 'react-i18next';

export interface MemberFormData {
  memberName: string;
  mobile: string;
  email?: string;
  password?: string;
  notes?: string;
}

interface MemberFormProps {
  onSubmit: (data: MemberFormData) => void;
  isLoading?: boolean;
}

export function MemberForm({ onSubmit, isLoading }: MemberFormProps) {
  const { t } = useTranslation();
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<MemberFormData>();

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
      {/* Member Name */}
      <div>
        <label htmlFor="memberName" className="block text-sm font-medium text-gray-700 mb-2">
          {t('form.memberName')} <span className="text-error-500">*</span>
        </label>
        <div className="relative">
          <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <User className="h-5 w-5 text-gray-400" />
          </div>
          <input
            id="memberName"
            type="text"
            {...register('memberName', {
              required: t('validation.nameRequired'),
            })}
            className={`
              block w-full pl-10 pr-3 py-2.5 border rounded-lg
              focus:ring-2 focus:ring-primary-500 focus:border-primary-500
              ${errors.memberName ? 'border-error-500' : 'border-gray-300'}
            `}
            placeholder={t('form.memberNamePlaceholder')}
            disabled={isLoading}
          />
        </div>
        {errors.memberName && (
          <p className="mt-1 text-sm text-error-600">{errors.memberName.message}</p>
        )}
      </div>

      {/* Mobile Number */}
      <div>
        <label htmlFor="mobile" className="block text-sm font-medium text-gray-700 mb-2">
          {t('form.mobile')} <span className="text-error-500">*</span>
        </label>
        <div className="relative">
          <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <Phone className="h-5 w-5 text-gray-400" />
          </div>
          <input
            id="mobile"
            type="tel"
            {...register('mobile', {
              required: t('validation.mobileRequired'),
              pattern: {
                value: /^\+254[17]\d{8}$/,
                message: t('validation.mobileInvalid'),
              },
            })}
            className={`
              block w-full pl-10 pr-3 py-2.5 border rounded-lg
              focus:ring-2 focus:ring-primary-500 focus:border-primary-500
              ${errors.mobile ? 'border-error-500' : 'border-gray-300'}
            `}
            placeholder={t('form.mobilePlaceholder')}
            disabled={isLoading}
          />
        </div>
        {errors.mobile && <p className="mt-1 text-sm text-error-600">{errors.mobile.message}</p>}
      </div>

      {/* Email (Optional) */}
      <div>
        <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
          {t('form.email')}
        </label>
        <div className="relative">
          <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <Mail className="h-5 w-5 text-gray-400" />
          </div>
          <input
            id="email"
            type="email"
            {...register('email', {
              pattern: {
                value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                message: t('validation.emailInvalid'),
              },
            })}
            className={`
              block w-full pl-10 pr-3 py-2.5 border rounded-lg
              focus:ring-2 focus:ring-primary-500 focus:border-primary-500
              ${errors.email ? 'border-error-500' : 'border-gray-300'}
            `}
            placeholder={t('form.emailPlaceholder')}
            disabled={isLoading}
          />
        </div>
        {errors.email && <p className="mt-1 text-sm text-error-600">{errors.email.message}</p>}
      </div>

      {/* PDF Password (Optional) */}
      <div>
        <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-2">
          {t('form.password')}
        </label>
        <div className="relative">
          <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <Lock className="h-5 w-5 text-gray-400" />
          </div>
          <input
            id="password"
            type="text"
            {...register('password')}
            className="block w-full pl-10 pr-3 py-2.5 border border-gray-300 rounded-lg
                     focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            placeholder={t('form.passwordPlaceholder')}
            disabled={isLoading}
          />
        </div>
      </div>

      {/* Notes (Optional) */}
      <div>
        <label htmlFor="notes" className="block text-sm font-medium text-gray-700 mb-2">
          {t('form.notes')}
        </label>
        <div className="relative">
          <div className="absolute top-3 left-0 pl-3 pointer-events-none">
            <FileText className="h-5 w-5 text-gray-400" />
          </div>
          <textarea
            id="notes"
            rows={3}
            {...register('notes')}
            className="block w-full pl-10 pr-3 py-2.5 border border-gray-300 rounded-lg
                     focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            placeholder={t('form.notesPlaceholder')}
            disabled={isLoading}
          />
        </div>
      </div>

      {/* Submit Button */}
      <button
        type="submit"
        disabled={isLoading}
        className="w-full bg-primary-600 hover:bg-primary-700 text-white font-medium 
                 py-3 px-6 rounded-lg transition-colors disabled:opacity-50 
                 disabled:cursor-not-allowed shadow-md hover:shadow-lg"
      >
        {isLoading ? t('button.generating') : t('button.generate')}
      </button>
    </form>
  );
}

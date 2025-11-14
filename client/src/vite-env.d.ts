/// <reference types="vite/client" />

interface ImportMetaEnv {
	readonly VITE_API_URL?: string;
	readonly VITE_ALLOW_ANY_MOBILE?: string;
}

interface ImportMeta {
	readonly env: ImportMetaEnv;
}

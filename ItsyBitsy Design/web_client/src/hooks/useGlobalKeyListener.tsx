// hooks/useGlobalKeyListener.ts
import { useEffect } from 'react';

export function useGlobalKeyListener(callback: (event: KeyboardEvent) => void) {
    useEffect(() => {
        const handler = (e: KeyboardEvent) => {
            callback(e);
        };
        window.addEventListener('keydown', handler);
        return () => {
            window.removeEventListener('keydown', handler);
        };
    }, [callback]);
}

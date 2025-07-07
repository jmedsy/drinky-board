// hooks/useGlobalKeyListener.ts
import { useEffect } from 'react';

export function useGlobalKeyListener(
    onKeyDown?: (event: KeyboardEvent) => void,
    onKeyUp?: (event: KeyboardEvent) => void
) {
    useEffect(() => {
        const keyDownHandler = (e: KeyboardEvent) => {
            onKeyDown?.(e);
        };

        const keyUpHandler = (e: KeyboardEvent) => {
            onKeyUp?.(e);
        };

        if (onKeyDown) {
            window.addEventListener('keydown', keyDownHandler);
        }

        if (onKeyUp) {
            window.addEventListener('keyup', keyUpHandler);
        }

        return () => {
            if (onKeyDown) {
                window.removeEventListener('keydown', keyDownHandler);
            }
            if (onKeyUp) {
                window.removeEventListener('keyup', keyUpHandler);
            }
        };
    }, [onKeyDown, onKeyUp]);
}

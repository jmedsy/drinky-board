'use client';

import { CacheProvider } from '@emotion/react';
import { CssBaseline, ThemeProvider } from '@mui/material';
import createEmotionCache from './emotionCache';
import theme from './theme';

const clientSideEmotionCache = createEmotionCache();

export default function MUIProvider({ children }: { children: React.ReactNode }) {
    return (
        <CacheProvider value={clientSideEmotionCache}>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                {children}
            </ThemeProvider>
        </CacheProvider>
    );
}

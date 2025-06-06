'use client';

import createCache from '@emotion/cache';

// This creates a cache for Emotion styles that MUI will use
export default function createEmotionCache() {
    return createCache({ key: 'css', prepend: true });
}

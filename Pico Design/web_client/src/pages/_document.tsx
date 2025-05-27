import createEmotionCache from '@/theme/createEmotionCache';
import theme from '@/theme/theme';
import type { EmotionCache } from '@emotion/cache';
import createEmotionServer from '@emotion/server/create-instance';
import type { AppProps } from 'next/app';
import Document, {
    DocumentContext,
    DocumentInitialProps,
    Head,
    Html,
    Main,
    NextScript,
} from 'next/document';
import * as React from 'react';

interface MyDocumentProps extends DocumentInitialProps {
    emotionStyleTags: React.JSX.Element[];
}

export default class MyDocument extends Document<MyDocumentProps> {
    render() {
        return (
            <Html lang="en">
                <Head>
                    <meta name="theme-color" content={theme.palette.primary.main} />
                    {this.props.emotionStyleTags}
                </Head>
                <body>
                    <Main />
                    <NextScript />
                </body>
            </Html>
        );
    }
}

MyDocument.getInitialProps = async (ctx: DocumentContext): Promise<MyDocumentProps> => {
    const originalRenderPage = ctx.renderPage;

    const cache = createEmotionCache();
    const { extractCriticalToChunks } = createEmotionServer(cache);


    ctx.renderPage = () =>
        originalRenderPage({
            enhanceApp: (App) =>
                function EnhanceApp(props: AppProps) {
                    const Enhanced = App as React.ComponentType<AppProps & { emotionCache: EmotionCache }>;
                    return <Enhanced {...props} emotionCache={cache} />;
                },
        });

    const initialProps = await Document.getInitialProps(ctx);
    const emotionStyles = extractCriticalToChunks(initialProps.html);
    const emotionStyleTags = emotionStyles.styles.map((style) => (
        <style
            data-emotion={`${style.key} ${style.ids.join(' ')}`}
            key={style.key}
            dangerouslySetInnerHTML={{ __html: style.css }}
        />
    ));

    return {
        ...initialProps,
        emotionStyleTags,
    };
};

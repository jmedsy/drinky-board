import Sidebar from "@/components/sidebar/Sidebar";
import WatermarkBlock from "@/components/WatermarkBlock";
import MUIProvider from "@/theme/MUIProvider";
import { Box } from "@mui/material";
import type { AppProps } from "next/app";

export default function App({ Component, pageProps }: AppProps) {
    return (
        <MUIProvider>
            <Sidebar />
            <Box component="main" sx={{ marginLeft: "340px", p: 3, position: "relative" }}>
                {/* Static watermark + quote */}
                <WatermarkBlock />

                {/* Page-specific content */}
                <Component {...pageProps} />
            </Box>
        </MUIProvider>
    );
}

import Sidebar from "@/components/Sidebar";
import MUIProvider from "@/theme/MUIProvider";
import { Box } from "@mui/material";
import type { AppProps } from "next/app";

export default function App({ Component, pageProps }: AppProps) {
    return (
        <MUIProvider>
            <Sidebar />
            <Box component="main" sx={{ marginLeft: '340px', p: 3 }}>
                <Component {...pageProps} />
            </Box>
        </MUIProvider>
    );
}

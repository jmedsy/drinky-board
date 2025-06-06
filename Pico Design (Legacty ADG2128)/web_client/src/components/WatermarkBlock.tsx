import { Box, Typography } from "@mui/material";
import { useEffect, useRef, useState } from "react";

const BASE_WIDTH = 600;

export default function WatermarkBlock() {
    const outerRef = useRef<HTMLDivElement>(null);
    const [scale, setScale] = useState(1);

    useEffect(() => {
        const node = outerRef.current;
        if (!node) return;

        const resizeObserver = new ResizeObserver(([entry]) => {
            const width = entry.contentRect.width;
            setScale(Math.min(1, width / BASE_WIDTH));
        });

        resizeObserver.observe(node);
        return () => resizeObserver.disconnect();
    }, []);

    return (
        <Box
            ref={outerRef}
            sx={{
                position: "absolute",
                top: "20vh",
                left: 0,
                width: "100%",
                maxWidth: "100%",
                overflow: "visible",
                zIndex: -1,
                pointerEvents: "none", // Optional: lets clicks pass through
            }}
        >
            {/* Safe padding to shift everything right */}
            <Box sx={{ pl: 5 }}>
                <Box
                    sx={{
                        width: "fit-content",
                        transform: `scale(${scale})`,
                        transformOrigin: "top left",
                    }}
                >
                    <Box
                        sx={{
                            width: `${BASE_WIDTH}px`,
                        }}
                    >
                        <Box
                            component="img"
                            src="/images/drinky_board_logo.svg"
                            alt="Drinky Board Logo"
                            sx={{
                                width: "100%",
                                height: "auto",
                                objectFit: "contain",
                                mb: 3,
                                pointerEvents: "none",
                            }}
                        />

                        <Box sx={{ width: "100%" }}>
                            <Typography
                                component="blockquote"
                                sx={{
                                    fontStyle: "italic",
                                    borderLeft: "4px solid",
                                    borderColor: "primary.main",
                                    pl: 2,
                                    color: "text.secondary",
                                    fontSize: "1rem",
                                    margin: 0,
                                }}
                            >
                                {`“It's not just about me and my dream of doing nothing. It's about all of us.”`}
                            </Typography>
                            <Typography
                                variant="body2"
                                sx={{
                                    mt: 1,
                                    textAlign: "right",
                                    color: "text.disabled",
                                    fontStyle: "italic",
                                    fontSize: "0.875rem",
                                }}
                            >
                                — Peter Gibbons, *Office Space*
                            </Typography>
                        </Box>
                    </Box>
                </Box>
            </Box>
        </Box>
    );
}

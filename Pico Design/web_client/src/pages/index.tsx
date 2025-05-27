import { Box, Typography } from '@mui/material';

export default function Home() {
    return (
        <>
            <Box sx={{ marginTop: 8, marginLeft: 8 }}>
                <Box
                    component="img"
                    src="/images/peter.png"
                    alt="Whatever"
                    sx={{ width: '100%', maxWidth: 600 }}
                />
                <Box
                    sx={{
                        my: 4,
                        maxWidth: 600, // keep it narrow like a real book/article quote
                    }}
                >
                    <Typography
                        component="blockquote"
                        sx={{
                            fontStyle: 'italic',
                            borderLeft: '4px solid',
                            borderColor: 'primary.main',
                            pl: 2,
                            color: 'text.secondary',
                        }}
                    >
                        {`“It's not just about me and my dream of doing nothing. It's about all of us.”`}
                    </Typography>
                    <Typography
                        variant="body2"
                        sx={{
                            mt: 1,
                            textAlign: 'right',
                            color: 'text.disabled',
                            fontStyle: 'italic',
                        }}
                    >
                        — Peter Gibbons, Office Space
                    </Typography>
                </Box>
            </Box>
        </>
    );
}

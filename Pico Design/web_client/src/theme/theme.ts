import { createTheme } from '@mui/material/styles';

const theme = createTheme({
    palette: {
        mode: 'light',
        primary: {
            main: '#1976d2',
        },
        secondary: {
            main: '#9c27b0',
        },
        background: {
            default: '#f9f9f9',
        },
    },
    typography: {
        fontFamily: '"Geist", "Helvetica", "Arial", sans-serif',
        h1: { fontSize: '2.5rem', fontWeight: 300 },
        h2: { fontSize: '2rem', fontWeight: 300 },
    },
    shape: {
        borderRadius: 10,
    },
    components: {
        MuiButton: {
            styleOverrides: {
                root: {
                    borderRadius: 10,
                    padding: '8px 16px',
                },
            },
        },
        MuiTextField: {
            defaultProps: {
                variant: 'outlined',
                margin: 'normal',
            },
        },
    },
});

export default theme;

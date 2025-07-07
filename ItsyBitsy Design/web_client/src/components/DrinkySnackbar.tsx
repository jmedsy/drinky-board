import type { AlertColor } from '@mui/material/Alert';
import Alert from '@mui/material/Alert';
import Snackbar, { SnackbarCloseReason } from '@mui/material/Snackbar';
import * as React from 'react';
import { createPortal } from 'react-dom';

interface DrinkySnackbarProps {
    open: boolean;
    setOpen: (value: boolean) => void;
    message: string;
    severity: AlertColor;
}

export default function DrinkySnackbar(props: DrinkySnackbarProps) {
    const [mounted, setMounted] = React.useState(false);

    React.useEffect(() => {
        setMounted(true);
    }, []);

    const handleClose = (
        event?: React.SyntheticEvent | Event,
        reason?: SnackbarCloseReason,
    ) => {
        if (reason === 'clickaway') {
            return;
        }

        props.setOpen(false);
    };

    const snackbarContent = (
        <Snackbar
            open={props.open}
            autoHideDuration={2000}
            onClose={handleClose}
            sx={{
                zIndex: 999999, // Extremely high z-index to ensure it's above everything
            }}
        >
            <Alert
                onClose={handleClose}
                severity={props.severity}
                variant="filled"
                sx={{ width: '100%' }}
            >
                {props.message}
            </Alert>
        </Snackbar>
    );

    // Only render the portal on the client side
    if (!mounted) {
        return null;
    }

    // Render the snackbar at the document root level using a portal
    return createPortal(snackbarContent, document.body);
}
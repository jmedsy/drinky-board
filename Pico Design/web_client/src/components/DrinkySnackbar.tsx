import Alert from '@mui/material/Alert';
import Snackbar, { SnackbarCloseReason } from '@mui/material/Snackbar';
import * as React from 'react';

interface DrinkySnackbarProps {
    open: boolean;
    setOpen: (value: boolean) => void;
    message: string;
}

export default function DrinkySnackbar(props: DrinkySnackbarProps) {

    const handleClose = (
        event?: React.SyntheticEvent | Event,
        reason?: SnackbarCloseReason,
    ) => {
        if (reason === 'clickaway') {
            return;
        }

        props.setOpen(false);
    };

    return (
        <div>
            <Snackbar open={props.open} autoHideDuration={2000} onClose={handleClose}>
                <Alert
                    onClose={handleClose}
                    severity="success"
                    variant="filled"
                    sx={{ width: '100%' }}
                >
                    {props.message}
                </Alert>
            </Snackbar>
        </div>
    );
}
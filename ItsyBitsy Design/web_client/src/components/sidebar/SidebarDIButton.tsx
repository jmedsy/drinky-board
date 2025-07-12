import { useGlobalKeyListener } from '@/hooks/useGlobalKeyListener';
import FiberManualRecordIcon from '@mui/icons-material/FiberManualRecord';
import KeyboardIcon from '@mui/icons-material/Keyboard';
import type { AlertColor } from '@mui/material/Alert';
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Typography from '@mui/material/Typography';
import { keyframes } from '@mui/system';
import * as React from 'react';
import DrinkySnackbar from '../DrinkySnackbar';

const flaskUrl = process.env.NEXT_PUBLIC_FLASK_BASE_URL;

const pulse = keyframes`
0%, 100% {
    transform: scale(1);
    opacity: 1;
}
50% {
    transform: scale(1.5);
    opacity: 0.6;
}
`;

export default function SidebarDIButton() {
    const [backdropOpen, setBackdropOpen] = React.useState(false);
    const [openDialog, setOpenDialog] = React.useState(false);
    const [snackbarMessage, setSnackbarMessage] = React.useState('');
    const [openSnackbar, setOpenSnackbar] = React.useState(false);
    const [snackbarSeverity, setSnackbarSeverity] = React.useState<AlertColor>('success');

    const sendKeyToFlask = async (code: string, data: unknown[], eventType: string = 'keydown') => {
        try {

            const res = await fetch(`${flaskUrl}/direct_input/listen`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    code: code,
                    data: data,
                    type: eventType
                })
            });

            if (!res.ok) {
                let responseData;
                try {
                    responseData = await res.json();
                    console.log('Error response data:', responseData);
                } catch (parseError) {
                    console.error('Failed to parse error response:', parseError);
                    // If we can't parse the response, assume device is disconnected
                    console.log('Device disconnected (unparseable response), closing Direct Input mode');
                    setBackdropOpen(false);
                    setSnackbarSeverity('error');
                    setSnackbarMessage('Device disconnected - Direct Input mode disabled');
                    setOpenSnackbar(true);
                    return;
                }

                // If device is disconnected, close the backdrop immediately and show message
                if (responseData.device_disconnected) {
                    console.log('Device disconnected, closing Direct Input mode');
                    setBackdropOpen(false);
                    setSnackbarSeverity('error');
                    setSnackbarMessage('Device disconnected - Direct Input mode disabled');
                    setOpenSnackbar(true);
                    return;
                }

                // For 500 errors, assume device is disconnected even if device_disconnected flag is not set
                if (res.status === 500) {
                    console.log('500 error - assuming device disconnected, closing Direct Input mode');
                    setBackdropOpen(false);
                    setSnackbarSeverity('error');
                    setSnackbarMessage('Device disconnected - Direct Input mode disabled');
                    setOpenSnackbar(true);
                    return;
                }

                // Handle other HTTP errors gracefully
                console.warn(`HTTP ${res.status} when sending key command`);
                return;
            }

            const responseData = await res.json();
            console.log('Flask response:', responseData);

            if (!responseData.success) {
                setSnackbarSeverity('error');
                setSnackbarMessage(responseData.message || 'Key command failed');
                setOpenSnackbar(true);
            }
        } catch (err) {
            console.error('API call failed:', err);
            setBackdropOpen(false);
            setSnackbarSeverity('error');
            setSnackbarMessage('Device connection lost - Direct Input mode disabled');
            setOpenSnackbar(true);
        }
    };

    const handleKeyDown = (e: KeyboardEvent) => {
        if (backdropOpen) {
            e.preventDefault();
            sendKeyToFlask(e.code, [], 'keydown');
        }
    };

    const handleKeyUp = (e: KeyboardEvent) => {
        if (backdropOpen) {
            sendKeyToFlask(e.code, [], 'keyup');
        }
    };

    // Global key listener for Direct Input mode
    useGlobalKeyListener(handleKeyDown, handleKeyUp);

    const handleButtonClick = () => {
        if (!backdropOpen) { // Prevents spacebar from reponening confirmation during DI mode
            setOpenDialog(true);
        }
    };

    const handleDIContinue = async () => {
        try {
            const data = await fetchDeviceStatus();
            if (data.connected) {
                setOpenDialog(false);
                setBackdropOpen(true);
            } else {
                setSnackbarSeverity('error');
                setSnackbarMessage(data.message);
                setOpenSnackbar(true);
            }
        } catch (err) {
            console.error('Failed to check device status:', err);
            setSnackbarSeverity('error');
            setSnackbarMessage('Failed to check device connection');
            setOpenSnackbar(true);
        }
    };

    const handleBackdropClick = () => {
        setBackdropOpen(false);
    };

    const fetchDeviceStatus = async () => {
        try {
            const response = await fetch(`${flaskUrl}/connection_status`);
            const data = await response.json();
            return data;
        } catch (err) {
            console.error(err);
            throw err;
        }
    };

    return (
        <>
            <ListItemButton onClick={handleButtonClick}>
                <ListItemIcon>
                    <KeyboardIcon />
                </ListItemIcon>
                <ListItemText primary='Direct Input Mode' />
            </ListItemButton>

            <Backdrop
                sx={{
                    backgroundColor: 'rgba(0, 0, 0, 0.93)',
                    zIndex: 9999,
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    position: 'fixed',
                    top: 0,
                    left: 0,
                    right: 0,
                    bottom: 0,
                }}
                open={backdropOpen}
                onClick={handleBackdropClick}
            >
                {backdropOpen && (
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                        <FiberManualRecordIcon
                            fontSize="large"
                            color='error'
                            sx={{ animation: `${pulse} 1s infinite` }}
                        />
                        <Typography variant="subtitle2" color="white" sx={{ userSelect: 'none' }}>
                            Click anywhere to exit Direct Input mode
                        </Typography>
                    </Box>
                )}
            </Backdrop>

            <Dialog
                open={openDialog}
                onClose={() => setOpenDialog(false)}
                aria-labelledby="alert-dialog-title"
                aria-describedby="alert-dialog-description"
            >
                <DialogTitle id="alert-dialog-title">
                    {"Enter Direct Input mode?"}
                </DialogTitle>
                <DialogContent>
                    <DialogContentText id="alert-dialog-description">
                        Browser will capture all keyboard activity and redirect it to the Drinky Board.
                    </DialogContentText>
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => setOpenDialog(false)}>Back</Button>
                    <Button onClick={handleDIContinue}>
                        Continue
                    </Button>
                </DialogActions>
            </Dialog>

            <DrinkySnackbar
                open={openSnackbar}
                setOpen={setOpenSnackbar}
                severity={snackbarSeverity}
                message={snackbarMessage}
            />
        </>
    );
}
import { useGlobalKeyListener } from '@/hooks/useGlobalKeyListener';
import type { AlertColor } from '@mui/material/Alert';
import * as React from 'react';
import DrinkySnackbar from '../DrinkySnackbar';
import { DIBackdrop, DIButton, DIDialog } from './directInput';
import { fetchDeviceStatus, listen } from './directInput/api';


export default function SidebarDIButton() {

    const [backdropOpen, setBackdropOpen] = React.useState(false);
    const [openDialog, setOpenDialog] = React.useState(false);
    const [snackbarMessage, setSnackbarMessage] = React.useState('');
    const [openSnackbar, setOpenSnackbar] = React.useState(false);
    const [snackbarSeverity, setSnackbarSeverity] = React.useState<AlertColor>('success');

    const sendKeyToFlask = async (code: string, data: unknown[], eventType: string = 'keydown') => {
        try {

            const res = await listen(code, data, eventType);

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
            const response = await fetchDeviceStatus();
            const data = await response.json();
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

    return (
        <>
            <DIButton onClick={handleButtonClick} />

            <DIBackdrop
                open={backdropOpen}
                onClick={handleBackdropClick}
            />

            <DIDialog
                open={openDialog}
                onClose={() => setOpenDialog(false)}
                onContinue={handleDIContinue}
            />

            <DrinkySnackbar
                open={openSnackbar}
                setOpen={setOpenSnackbar}
                severity={snackbarSeverity}
                message={snackbarMessage}
            />
        </>
    );
}
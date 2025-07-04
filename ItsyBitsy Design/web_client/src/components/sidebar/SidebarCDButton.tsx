import UsbIcon from '@mui/icons-material/Usb';
import type { AlertColor } from '@mui/material/Alert';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import * as React from 'react';
import DrinkySnackbar from '../DrinkySnackbar';

const flaskUrl = process.env.NEXT_PUBLIC_FLASK_BASE_URL;

export default function SidebarCDButton() {
    const [openSnackbar, setOpenSnackbar] = React.useState(false);
    const [snackbarMessage, setSnackbarMessage] = React.useState('');
    const [snackbarSeverity, setSnackbarSeverity] = React.useState<AlertColor>('success');

    const handleClickCD = async () => {
        try {
            const res = await fetch(`${flaskUrl}/find_itsybitsy_ports`);
            const data = await res.json();
            setSnackbarSeverity(data.success == true ? 'success' : 'error');
            setSnackbarMessage(data.message);
        } catch (err) {
            console.error('API call failed:', err);
        }
        setOpenSnackbar(true)
    }

    return (
        <>
            <ListItemButton onClick={() => handleClickCD()}>
                <ListItemIcon>
                    <UsbIcon />
                </ListItemIcon>
                <ListItemText primary='Check Device' />
            </ListItemButton>
            <DrinkySnackbar open={openSnackbar} setOpen={setOpenSnackbar} severity={snackbarSeverity} message={snackbarMessage} />
        </>
    )
}
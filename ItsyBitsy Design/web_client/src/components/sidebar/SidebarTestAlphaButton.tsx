import type { AlertColor } from '@mui/material/Alert';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import * as React from 'react';
import DrinkySnackbar from '../DrinkySnackbar';

const flaskUrl = process.env.NEXT_PUBLIC_FLASK_BASE_URL;

export default function SidebarTestAlphaButton() {
    const [openSnackbar, setOpenSnackbar] = React.useState(false);
    const [snackbarMessage, setSnackbarMessage] = React.useState('');
    const [snackbarSeverity, setSnackbarSeverity] = React.useState<AlertColor>('success');

    const handleClickAlphabet = async () => {
        try {
            const res = await fetch(`${flaskUrl}/outputTests/alphabet`);
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
            <ListItemButton onClick={() => handleClickAlphabet()} sx={{ pl: 6 }}>
                <ListItemText primary='Alphabet' />
            </ListItemButton>
            <DrinkySnackbar open={openSnackbar} setOpen={setOpenSnackbar} severity={snackbarSeverity} message={snackbarMessage} />
        </>
    )
}
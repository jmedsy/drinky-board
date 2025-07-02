import CheckIcon from '@mui/icons-material/Check';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import InfoIcon from '@mui/icons-material/Info';
import KeyboardIcon from '@mui/icons-material/Keyboard';
import PeopleIcon from '@mui/icons-material/People';
import UsbIcon from '@mui/icons-material/Usb';
import type { AlertColor } from '@mui/material/Alert';
import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import * as React from 'react';
import DrinkySnackbar from './DrinkySnackbar';
import SingleKeyDialog from './SingleKeyDialog';

const flaskUrl = process.env.NEXT_PUBLIC_FLASK_BASE_URL;

export default function NestedList() {
    const [open, setOpen] = React.useState(false);
    const [singleKeyOpen, setSingleKeyOpen] = React.useState(false);
    const [snackbarMessage, setSnackbarMessage] = React.useState('');
    const [openSnackbar, setOpenSnackbar] = React.useState(false);
    const [snackbarSeverity, setSnackbarSeverity] = React.useState<AlertColor>('success');

    const handleClickCC = async () => {
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

    const handleClick = () => {
        setOpen(!open);
    };

    return (
        <Box
            sx={{
                width: 340,
                height: '100vh',
                position: 'fixed',
                left: 0,
                top: 0,
                // bgcolor: 'background.paper',
                borderRight: 1,
                borderColor: 'divider',
            }}
        >
            <List>
                <ListItemButton onClick={() => handleClickCC()}>
                    <ListItemIcon>
                        <UsbIcon />
                    </ListItemIcon>
                    <ListItemText primary="Check Connection" />
                </ListItemButton>
                <ListItemButton>
                    <ListItemIcon>
                        <KeyboardIcon />
                    </ListItemIcon>
                    <ListItemText primary="Direct Input Mode" />
                </ListItemButton>
                <ListItemButton onClick={handleClick}>
                    <ListItemIcon>
                        <CheckIcon />
                    </ListItemIcon>
                    <ListItemText primary="Output Tests" />
                    {open ? <ExpandLess /> : <ExpandMore />}
                </ListItemButton>
                <Collapse in={open} timeout={0} unmountOnExit>
                    <List component="div" disablePadding>
                        <ListItemButton onClick={() => setSingleKeyOpen(true)} sx={{ pl: 4 }}>
                            {/* <ListItemIcon >
                                <FontDownloadIcon />
                            </ListItemIcon> */}
                            <ListItemText primary="Single Key" />
                        </ListItemButton>
                        <ListItemButton onClick={() => handleClickAlphabet()} sx={{ pl: 4 }}>
                            {/* <ListItemIcon>
                                <AbcIcon />
                            </ListItemIcon> */}
                            <ListItemText primary="Alphabet" />
                        </ListItemButton>
                        <ListItemButton sx={{ pl: 4 }}>
                            {/* <ListItemIcon>
                                <NumbersIcon />
                            </ListItemIcon> */}
                            <ListItemText primary="Keyboard Digits" />
                        </ListItemButton>
                        <ListItemButton sx={{ pl: 4 }}>
                            {/* <ListItemIcon>
                                <NumbersIcon />
                            </ListItemIcon> */}
                            <ListItemText primary="Numpad Digits" />
                        </ListItemButton>
                    </List>
                </Collapse>
                <ListItemButton>
                    <ListItemIcon>
                        <PeopleIcon />
                    </ListItemIcon>
                    <ListItemText primary="Typing Profiles" />
                </ListItemButton>
                <ListItemButton>
                    <ListItemIcon>
                        <InfoIcon />
                    </ListItemIcon>
                    <ListItemText primary="About" />
                </ListItemButton>
            </List>

            <DrinkySnackbar open={openSnackbar} setOpen={setOpenSnackbar} severity={snackbarSeverity} message={snackbarMessage} />
            <SingleKeyDialog open={singleKeyOpen} setOpen={setSingleKeyOpen} />
        </Box>
    );
}

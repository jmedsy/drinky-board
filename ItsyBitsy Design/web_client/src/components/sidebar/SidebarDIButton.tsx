import FiberManualRecordIcon from '@mui/icons-material/FiberManualRecord';
import KeyboardIcon from '@mui/icons-material/Keyboard';
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

    // Use a ref to persist state across re-mounts
    const backdropRef = React.useRef(false);

    // Initialize state from ref on mount
    React.useEffect(() => {
        if (backdropRef.current) {
            setBackdropOpen(true);
        }
    }, []);

    // Update ref when state changes
    React.useEffect(() => {
        backdropRef.current = backdropOpen;
    }, [backdropOpen]);

    const handleDIContinue = () => {
        setOpenDialog(false);
        setBackdropOpen(true);
    }

    return (
        <>
            <ListItemButton onClick={() => setOpenDialog(true)}>
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
                onClick={() => setBackdropOpen(false)}
            >
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                    <FiberManualRecordIcon
                        fontSize="large"
                        color="error"
                        sx={{ animation: `${pulse} 1s infinite` }}
                    />
                    <Typography
                        variant="subtitle2"
                        color="white"
                        sx={{
                            userSelect: 'none',
                            WebkitUserSelect: 'none',
                            MozUserSelect: 'none',
                            msUserSelect: 'none',
                        }}
                    >
                        Click anywhere to exit Direct Input mode
                    </Typography>
                </Box>
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
                    <Button onClick={handleDIContinue} autoFocus>
                        Continue
                    </Button>
                </DialogActions>
            </Dialog>
        </>
    )
}
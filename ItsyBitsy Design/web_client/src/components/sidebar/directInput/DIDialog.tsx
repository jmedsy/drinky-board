import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';

interface DIDialogProps {
    open: boolean;
    onClose: () => void;
    onContinue: () => void;
}

export default function DIDialog({ open, onClose, onContinue }: DIDialogProps) {
    return (
        <Dialog
            open={open}
            onClose={onClose}
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
                <Button onClick={onClose}>Back</Button>
                <Button onClick={onContinue}>
                    Continue
                </Button>
            </DialogActions>
        </Dialog>
    );
}

import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';

export interface SingleKeyDialogProps {
    open: boolean;
    setOpen: (value: boolean) => void;
}

export default function SingleKeyDialog(props: SingleKeyDialogProps) {
    return (
        <Dialog onClose={() => props.setOpen(false)} open={props.open}>
            <DialogTitle>Output Tests: Single Key</DialogTitle>
            <DialogContent>
                asdf
            </DialogContent>
        </Dialog>
    );
}
import Box from '@mui/material/Box';
import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select, { SelectChangeEvent } from '@mui/material/Select';

interface SingleKeyDialogProps {
    open: boolean;
    setOpen: (value: boolean) => void;
}

const handleChange = (event: SelectChangeEvent) => {
    // setAge(event.target.value as string);
    window.alert(event);
};

export default function SingleKeyDialog(props: SingleKeyDialogProps) {
    return (
        <Dialog onClose={() => props.setOpen(false)} open={props.open}>
            <DialogTitle>Output Tests: Single Key</DialogTitle>
            <DialogContent>
                <Box sx={{ minWidth: 120 }}>
                    <FormControl fullWidth>
                        <InputLabel id="demo-simple-select-label">Age</InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            //value={age}
                            label="Age"
                            onChange={handleChange}
                        >
                            <MenuItem value={10}>Ten</MenuItem>
                            <MenuItem value={20}>Twenty</MenuItem>
                            <MenuItem value={30}>Thirty</MenuItem>
                        </Select>
                    </FormControl>
                </Box>
            </DialogContent>
        </Dialog>
    );
}
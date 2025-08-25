import KeyboardIcon from '@mui/icons-material/Keyboard';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';

interface DIButtonProps {
    onClick: () => void;
}

export default function DIButton({ onClick }: DIButtonProps) {
    return (
        <ListItemButton onClick={onClick}>
            <ListItemIcon>
                <KeyboardIcon />
            </ListItemIcon>
            <ListItemText primary='Direct Input Mode' />
        </ListItemButton>
    );
}

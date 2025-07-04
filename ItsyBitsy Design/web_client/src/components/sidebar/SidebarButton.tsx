// import * as React from 'react';
import { SvgIconComponent } from '@mui/icons-material';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';

interface SidebarButtonProps {
    icon: SvgIconComponent;
    text: string;
}

export default function SidebarButton(props: SidebarButtonProps) {
    // const [backdropOpen, setBackdropOpen] = React.useState(false);

    return (
        <>
            <ListItemButton>
                <ListItemIcon>
                    <props.icon />
                </ListItemIcon>
                <ListItemText primary={props.text} />
            </ListItemButton>
        </>
    )
}
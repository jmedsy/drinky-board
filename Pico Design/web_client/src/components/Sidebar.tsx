// import { Box, List, ListItemButton, ListItemText } from '@mui/material';
import AbcIcon from '@mui/icons-material/Abc';
import CheckIcon from '@mui/icons-material/Check';
import FontDownloadIcon from '@mui/icons-material/FontDownload';
import KeyboardIcon from '@mui/icons-material/Keyboard';
import NumbersIcon from '@mui/icons-material/Numbers';
import UsbIcon from '@mui/icons-material/Usb';
import { Box } from '@mui/material';

import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import Collapse from '@mui/material/Collapse';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
// import ListSubheader from '@mui/material/ListSubheader';
import * as React from 'react';

export default function NestedList() {
    const [open, setOpen] = React.useState(false);

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
                <ListItemButton>
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
                        <ListItemButton sx={{ pl: 4 }}>
                            <ListItemIcon>
                                <FontDownloadIcon />
                            </ListItemIcon>
                            <ListItemText primary="Key A" />
                        </ListItemButton>
                        <ListItemButton sx={{ pl: 4 }}>
                            <ListItemIcon>
                                <AbcIcon />
                            </ListItemIcon>
                            <ListItemText primary="Alphabet" />
                        </ListItemButton>
                        <ListItemButton sx={{ pl: 4 }}>
                            <ListItemIcon>
                                <NumbersIcon />
                            </ListItemIcon>
                            <ListItemText primary="Keyboard Digits" />
                        </ListItemButton>
                        <ListItemButton sx={{ pl: 4 }}>
                            <ListItemIcon>
                                <NumbersIcon />
                            </ListItemIcon>
                            <ListItemText primary="Numpad Digits" />
                        </ListItemButton>
                    </List>
                </Collapse>
            </List>
        </Box>
    );
}

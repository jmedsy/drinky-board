import CheckIcon from '@mui/icons-material/Check';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import InfoIcon from '@mui/icons-material/Info';
import PeopleIcon from '@mui/icons-material/People';
import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import * as React from 'react';
import ConnectionStatus from './ConnectionStatus';
import SidebarButton from './SidebarButton';
import SidebarDIButton from './SidebarDIButton';
import SidebarTestAlphaButton from './SidebarTestAlphaButton';

export default function NestedList() {
    const [openTests, setOpenTests] = React.useState(false);

    const toggleTests = () => {
        setOpenTests(!openTests);
    }

    return (
        <Box
            sx={{
                width: 340,
                height: '100vh',
                position: 'fixed',
                left: 0,
                top: 0,
                borderRight: 1,
                borderColor: 'divider',
            }}
        >
            <List>
                <ConnectionStatus />
                <SidebarDIButton />
                <ListItemButton onClick={() => toggleTests()}>
                    <ListItemIcon>
                        <CheckIcon />
                    </ListItemIcon>
                    <ListItemText primary="Output Tests" />
                    {openTests ? <ExpandLess /> : <ExpandMore />}
                </ListItemButton>
                <Collapse in={openTests} timeout={0} unmountOnExit>
                    <List component="div" disablePadding>
                        <SidebarTestAlphaButton />
                    </List>
                </Collapse>
                <SidebarButton icon={PeopleIcon} text='Typing Profiles' />
                <SidebarButton icon={InfoIcon} text='About' />
            </List>
        </Box>
    );
}

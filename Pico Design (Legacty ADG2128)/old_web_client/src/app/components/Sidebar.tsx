import { Box, List, ListItem, ListItemButton, ListItemText } from '@mui/material';

export default function Sidebar() {
    return (
        <Box
            sx={{
                width: 240,
                height: '100vh',
                position: 'fixed',
                //bgcolor: 'background.paper',
                borderRight: 1,
                borderColor: 'divider',
            }}
        >
            <List>
                <ListItem disablePadding>
                    <ListItemButton>
                        <ListItemText primary="Home" />
                    </ListItemButton>
                </ListItem>
                <ListItem disablePadding>
                    <ListItemButton>
                        <ListItemText primary="Tools" />
                    </ListItemButton>
                </ListItem>
            </List>
        </Box>
    );
}

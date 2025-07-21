import SettingsSuggestIcon from '@mui/icons-material/SettingsSuggest';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Typography from '@mui/material/Typography';
import * as React from 'react';
import DraggableList from '../DraggableList';

export default function SidebarProfilesButton() {
    const [openDialog, setOpenDialog] = React.useState(false);

    // Sample items for the draggable list
    const sampleItems = [
        <Box key="1" sx={{ p: 2, backgroundColor: '#e3f2fd', borderRadius: 1, textAlign: 'center' }}>
            <Typography variant="h6">Action 1</Typography>
            <Typography variant="body2">Type some text</Typography>
        </Box>,
        <Box key="2" sx={{ p: 2, backgroundColor: '#f3e5f5', borderRadius: 1, textAlign: 'center' }}>
            <Typography variant="h6">Action 2</Typography>
            <Typography variant="body2">Wait 500ms</Typography>
        </Box>,
        <Box key="3" sx={{ p: 2, backgroundColor: '#e8f5e8', borderRadius: 1, textAlign: 'center' }}>
            <Typography variant="h6">Action 3</Typography>
            <Typography variant="body2">Press Ctrl+C</Typography>
        </Box>,
        <Box key="4" sx={{ p: 2, backgroundColor: '#fff3e0', borderRadius: 1, textAlign: 'center' }}>
            <Typography variant="h6">Action 4</Typography>
            <Typography variant="body2">Type file content</Typography>
        </Box>
    ];

    const handleButtonClick = () => {
        setOpenDialog(true);
    }

    return (
        <>
            <ListItemButton onClick={handleButtonClick}>
                <ListItemIcon>
                    <SettingsSuggestIcon />
                </ListItemIcon>
                <ListItemText primary='Sequences' />
            </ListItemButton>

            <Dialog
                open={openDialog}
                aria-labelledby='alert-dialog-title'
                aria-describedby='alert-dialog-description'
                maxWidth='md'
                fullWidth
                disableEscapeKeyDown
            >
                <DialogContent>
                    <Box sx={{ display: 'flex', gap: 2 }}>
                        <Box sx={{ flex: '0 0 30%' }}>
                            <Box sx={{ mt: 2, display: 'flex', flexDirection: 'column' }}>
                                <Box sx={{
                                    height: '400px',
                                    overflowY: 'auto',
                                    border: '1px solid #e0e0e0',
                                    borderRadius: 1,
                                    p: 1,
                                    backgroundColor: '#fafafa'
                                }}>

                                </Box>
                            </Box>
                        </Box>
                        <Box sx={{ flex: 1, display: 'flex', alignItems: 'center' }}>
                            <Box sx={{ width: '100%', p: 2 }}>
                                <DraggableList
                                    // height="300px"
                                    items={sampleItems}
                                    onReorder={(oldIdx, newIdx) => console.log(`moved item from ${oldIdx} to ${newIdx}`)}
                                />
                            </Box>
                        </Box>
                    </Box>
                </DialogContent>
                <DialogActions>
                    <Box sx={{ flex: 1 }} />
                    <Button onClick={() => setOpenDialog(false)}>Back</Button>
                    <Button variant='contained' color='primary'>
                        Save
                    </Button>
                </DialogActions>
            </Dialog>
        </>
    );
}
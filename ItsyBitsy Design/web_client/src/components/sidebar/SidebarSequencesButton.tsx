import SettingsSuggestIcon from '@mui/icons-material/SettingsSuggest';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import * as React from 'react';
import DraggableList, { DraggableItem } from '../DraggableList';




export default function SidebarProfilesButton() {
    const [openDialog, setOpenDialog] = React.useState(false);
    // const [wasOriginallyActive, setWasOriginallyActive] = React.useState(false);
    const [formData, setFormData] = React.useState({
        name: '',
        wpm: 60,
        wpmVariation: 10,
        keyDuration: 100,
        keyDurationVariation: 20,
        description: '',
        isActive: false
    });

    // Custom setter to prevent reordering
    const updateSequenceActions = React.useCallback((newActions: DraggableItem[]) => {
        console.log('updateSequenceActions called with:', newActions.map(item => `${item.type} (${item.id})`));
    }, []);



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
                                <Typography variant="h6" sx={{ mb: 2 }}>
                                    {'New Profile'}
                                </Typography>
                                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                                    <TextField
                                        label="Sequence Name"
                                        value={formData.name}
                                        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                                        size="small"
                                    />

                                    <DraggableList
                                        onItemsChange={updateSequenceActions}
                                        onAddItem={(type?: string) => {
                                            const newAction: DraggableItem = {
                                                id: Date.now().toString(),
                                                type: type || 'New Action',
                                                description: 'Click to edit'
                                            };
                                            console.log('Adding new action:', newAction);
                                        }}
                                        height="300px"
                                        title=""
                                        addItemText="+ Add Action"
                                    />
                                </Box>
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
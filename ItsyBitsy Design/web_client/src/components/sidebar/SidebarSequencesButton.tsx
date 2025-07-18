import DeleteIcon from '@mui/icons-material/Delete';
import SettingsSuggestIcon from '@mui/icons-material/SettingsSuggest';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import IconButton from '@mui/material/IconButton';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Paper from '@mui/material/Paper';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import * as React from 'react';
import DraggableList from '../DraggableList';

const flaskUrl = process.env.NEXT_PUBLIC_FLASK_BASE_URL;

interface TypingProfile {
    name: string;
    wpm: number;
    wpmVariation: number;
    keyDuration: number;
    keyDurationVariation: number;
    description?: string;
    created: string;
    isActive: boolean;
}

interface Profile {
    filename: string;
    data: TypingProfile;
}



export default function SidebarProfilesButton() {
    const [openDialog, setOpenDialog] = React.useState(false);
    const [saveBtnEnabled, setSaveBtnEnabled] = React.useState(false);
    const [profiles, setProfiles] = React.useState<Profile[]>([]);
    const [selectedProfile, setSelectedProfile] = React.useState<string | null>(null);
    const [isAddNewSelected, setIsAddNewSelected] = React.useState(false);
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
    const [sequenceActions, setSequenceActions] = React.useState<React.ReactNode[]>([]);

    // Custom setter to prevent reordering
    const updateSequenceActions = React.useCallback((newActions: React.ReactNode[]) => {
        setSequenceActions(newActions);
    }, []);

    /* API function */
    const postProfile = async () => {
        const profileData = {
            name: formData.name,
            wpm: formData.wpm,
            wpmVariation: formData.wpmVariation,
            keyDuration: formData.keyDuration,
            keyDurationVariation: formData.keyDurationVariation,
            description: formData.description,
            isActive: formData.isActive
        };

        const res = await fetch(`${flaskUrl}/profiles/add`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(profileData)
        });

        return res;
    }

    /* API function */
    const putProfile = async (filename: string) => {
        const profileData = {
            name: formData.name,
            wpm: formData.wpm,
            wpmVariation: formData.wpmVariation,
            keyDuration: formData.keyDuration,
            keyDurationVariation: formData.keyDurationVariation,
            description: formData.description,
            isActive: formData.isActive
        };

        const res = await fetch(`${flaskUrl}/profiles/edit/${filename}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(profileData)
        });

        return res;
    }

    /* API function */
    const getAllProfiles = async () => {
        const res = await fetch(`${flaskUrl}/profiles/get_all`);
        return res;
    }

    /* API function */
    const deleteProfile = async (filename: string) => {
        const res = await fetch(`${flaskUrl}/profiles/delete/${filename}`, {
            method: 'DELETE'
        });
        return res;
    }

    /* API Function */
    const deactivateExcept = async (filename: string) => {
        const res = await fetch(`${flaskUrl}/profiles/deactivateExcept/${filename}`, {
            method: 'PUT',
        });
        return res;
    }

    const handleButtonClick = () => {
        refreshProfiles();
        setOpenDialog(true);

        // Auto-populate the DraggableList with actual profiles
        // We'll convert profiles to DraggableItems after the profiles are loaded
    }

    const handleAddNewClick = () => {
        setSaveBtnEnabled(true);
        setSelectedProfile(null);
        setIsAddNewSelected(true);
        setFormData({
            name: '',
            wpm: 60,
            wpmVariation: 10,
            keyDuration: 100,
            keyDurationVariation: 20,
            description: '',
            isActive: false
        });
        // Clear the sequence actions when adding new
        setSequenceActions([]);
    };

    const handleProfileSelect = (profile: Profile) => {
        setSelectedProfile(profile.filename);
        setSaveBtnEnabled(true);
        setIsAddNewSelected(false);
        // setWasOriginallyActive(profile.data.isActive);
        setFormData({
            ...profile.data,
            description: profile.data.description || ''
        });

        // Populate the DraggableList with actions based on the profile
        const profileActions: React.ReactNode[] = [
            <Paper
                key="wpm-action"
                sx={{
                    height: '60px',
                    mb: 1,
                    p: 2,
                    backgroundColor: '#fefefe',
                    border: '1px solid #e8e8e8',
                    borderRadius: 1,
                    cursor: 'grab',
                    '&:active': { cursor: 'grabbing' },
                    '&:hover': { backgroundColor: '#f5f5f5' },
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'space-between',
                    position: 'relative',
                    userSelect: 'none',
                    transition: 'all 0.2s ease'
                }}
            >
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <Typography variant="body2" noWrap sx={{ fontWeight: 'bold', maxWidth: '50%' }}>
                        Set WPM
                    </Typography>
                </Box>
                <Box sx={{ fontSize: '0.7rem', color: '#666' }}>
                    {profile.data.wpm} ± {profile.data.wpmVariation}
                </Box>
            </Paper>,
            <Paper
                key="key-duration-action"
                sx={{
                    height: '60px',
                    mb: 1,
                    p: 2,
                    backgroundColor: '#fefefe',
                    border: '1px solid #e8e8e8',
                    borderRadius: 1,
                    cursor: 'grab',
                    '&:active': { cursor: 'grabbing' },
                    '&:hover': { backgroundColor: '#f5f5f5' },
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'space-between',
                    position: 'relative',
                    userSelect: 'none',
                    transition: 'all 0.2s ease'
                }}
            >
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <Typography variant="body2" noWrap sx={{ fontWeight: 'bold', maxWidth: '50%' }}>
                        Set Key Duration
                    </Typography>
                </Box>
                <Box sx={{ fontSize: '0.7rem', color: '#666' }}>
                    {profile.data.keyDuration} ± {profile.data.keyDurationVariation}ms
                </Box>
            </Paper>,
            <Paper
                key="profile-description-action"
                sx={{
                    height: '60px',
                    mb: 1,
                    p: 2,
                    backgroundColor: '#fefefe',
                    border: '1px solid #e8e8e8',
                    borderRadius: 1,
                    cursor: 'grab',
                    '&:active': { cursor: 'grabbing' },
                    '&:hover': { backgroundColor: '#f5f5f5' },
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'space-between',
                    position: 'relative',
                    userSelect: 'none',
                    transition: 'all 0.2s ease'
                }}
            >
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <Typography variant="body2" noWrap sx={{ fontWeight: 'bold', maxWidth: '50%' }}>
                        Profile Description
                    </Typography>
                </Box>
                <Box sx={{ fontSize: '0.7rem', color: '#666' }}>
                    {profile.data.description || 'No description'}
                </Box>
            </Paper>
        ];
        setSequenceActions(profileActions);
    };

    const resetToInitialState = () => {
        setSelectedProfile(null);
        setIsAddNewSelected(false);
        setSaveBtnEnabled(false);
        // setWasOriginallyActive(false);
        setFormData({
            name: '',
            wpm: 60,
            wpmVariation: 10,
            keyDuration: 100,
            keyDurationVariation: 20,
            description: '',
            isActive: false
        });
        // Don't clear sequence actions here - let them persist
    }

    const handleSaveBtnClick = async () => {
        setSaveBtnEnabled(false);

        try {
            const res = selectedProfile ? await putProfile(selectedProfile) : await postProfile();
            const data = await res.json();

            if (!data.success) {
                throw new Error(data.message);
            } else {
                console.log(`Profile ${selectedProfile ? 'edited' : 'saved'} successfully:`, data);
            }

            // Only deactivate others if this profile is being set as active
            if (formData.isActive) {
                try {
                    const res2 = await deactivateExcept(data.filename);
                    const data2 = await res2.json();

                    if (!data2.success) {
                        throw new Error(data2.message);
                    } else {
                        console.log(data2.message, data);
                    }
                } catch (err) {
                    console.error('API call failed:', err);
                }
            }

            refreshProfiles();
            resetToInitialState();
        } catch (err) {
            console.error('API call failed:', err);
            // Re-enable save button on error
            setSaveBtnEnabled(true);
        }
    }

    const deleteHandler = async (filename: string) => {
        try {
            const res = await deleteProfile(filename);
            const data = await res.json();

            if (!data.success) {
                throw new Error(data.message);
            } else {
                console.log('Profile deleted successfully:', data);
                refreshProfiles();
            }
        } catch (err) {
            console.error('Delete API call failed:', err);
        }
    }

    const refreshProfiles = async () => {
        try {
            const res = await getAllProfiles();
            const data = await res.json();

            if (!data.success) {
                throw new Error(data.message);
            } else {
                const profileList = data.profiles.map((p: Profile) => p);
                // Sort profiles alphabetically by name
                profileList.sort((a: Profile, b: Profile) => a.data.name.localeCompare(b.data.name));
                setProfiles(profileList);

                // Convert profiles to React nodes for the list
                const profileReactNodes: React.ReactNode[] = profileList.map((profile: Profile) => (
                    <Paper
                        key={profile.filename}
                        sx={{
                            height: '60px',
                            mb: 1,
                            p: 2,
                            backgroundColor: '#fefefe',
                            border: '1px solid #e8e8e8',
                            borderRadius: 1,
                            cursor: 'grab',
                            '&:active': { cursor: 'grabbing' },
                            '&:hover': { backgroundColor: '#f5f5f5' },
                            display: 'flex',
                            flexDirection: 'column',
                            justifyContent: 'space-between',
                            position: 'relative',
                            userSelect: 'none',
                            transition: 'all 0.2s ease'
                        }}
                    >
                        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                            <Typography variant="body2" noWrap sx={{ fontWeight: 'bold', maxWidth: '50%' }}>
                                {profile.data.name}
                            </Typography>
                            <Typography variant="caption" sx={{ color: profile.data.isActive ? 'green' : 'gray', mr: 3 }}>
                                {profile.data.isActive ? 'Active' : 'Inactive'}
                            </Typography>
                        </Box>
                        <Box sx={{ fontSize: '0.7rem', color: '#666' }}>
                            {profile.data.wpm}±{profile.data.wpmVariation} WPM, {profile.data.keyDuration}±{profile.data.keyDurationVariation}ms
                        </Box>
                    </Paper>
                ));
                setSequenceActions(profileReactNodes);

                // Always reset to initial disabled state
                resetToInitialState();
            }
        } catch (err) {
            console.error('API call failed:', err);
        }
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
                                    {profiles.map((p, index) => (
                                        <Paper
                                            key={index}
                                            sx={{
                                                height: '60px',
                                                mb: 1,
                                                p: 2,
                                                backgroundColor: selectedProfile === p.filename ? '#e3f2fd' : '#fefefe',
                                                border: selectedProfile === p.filename ? '1px solid #2196f3' : '1px solid #e8e8e8',
                                                display: 'flex',
                                                flexDirection: 'column',
                                                justifyContent: 'space-between',
                                                position: 'relative',
                                                cursor: 'pointer',
                                                userSelect: 'none',
                                                '&:hover': {
                                                    backgroundColor: selectedProfile === p.filename ? '#e3f2fd' : '#f5f5f5'
                                                }
                                            }}
                                            onClick={() => handleProfileSelect(p)}
                                        >
                                            <Box sx={{
                                                position: 'absolute',
                                                top: 4,
                                                right: 4,
                                                display: 'flex',
                                                gap: 0.5
                                            }}>
                                                <IconButton size="small" sx={{ p: 0.5 }} onClick={() => deleteHandler(p.filename)}>
                                                    <DeleteIcon fontSize="small" />
                                                </IconButton>
                                            </Box>
                                            <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                                <Typography variant="body2" noWrap sx={{ fontWeight: 'bold', maxWidth: '50%' }}>
                                                    {p.data.name}
                                                </Typography>
                                                <Typography variant="caption" sx={{ color: p.data.isActive ? 'green' : 'gray', mr: 3 }}>
                                                    {p.data.isActive ? 'Active' : 'Inactive'}
                                                </Typography>
                                            </Box>
                                            <Box sx={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.7rem', color: '#666' }}>
                                                <span>WPM: {p.data.wpm}±{p.data.wpmVariation}</span>
                                                <span>Duration: {p.data.keyDuration}±{p.data.keyDurationVariation}ms</span>
                                            </Box>
                                        </Paper>
                                    ))}

                                    <Paper
                                        sx={{
                                            height: '60px',
                                            mb: 1,
                                            backgroundColor: isAddNewSelected ? '#e3f2fd' : '#fefefe',
                                            border: isAddNewSelected ? '1px solid #2196f3' : '1px solid #e8e8e8',
                                            cursor: 'pointer',
                                            '&:hover': {
                                                backgroundColor: isAddNewSelected ? '#e3f2fd' : '#f5f5f5'
                                            }
                                        }}
                                    >
                                        <Button
                                            variant='text'
                                            sx={{
                                                width: '100%',
                                                height: '100%',
                                                borderRadius: 0
                                            }}
                                            onClick={() => handleAddNewClick()}
                                        >
                                            Add New
                                        </Button>
                                    </Paper>
                                </Box>
                            </Box>
                        </Box>
                        <Box sx={{ flex: 1, display: 'flex', alignItems: 'center' }}>
                            <Box sx={{ width: '100%', p: 2 }}>
                                <Typography variant="h6" sx={{ mb: 2 }}>
                                    {selectedProfile ? 'Edit Profile' : 'New Profile'}
                                </Typography>
                                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                                    <TextField
                                        label="Sequence Name"
                                        value={formData.name}
                                        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                                        size="small"
                                        disabled={!saveBtnEnabled}
                                    />

                                    <DraggableList
                                        items={sequenceActions}
                                        onReorder={updateSequenceActions}
                                        height="300px"
                                    />
                                </Box>
                            </Box>
                        </Box>
                    </Box>
                </DialogContent>
                <DialogActions>
                    <Box sx={{ flex: 1 }} />
                    <Button onClick={() => setOpenDialog(false)}>Back</Button>
                    <Button variant='contained' color='primary' disabled={!saveBtnEnabled} onClick={() => handleSaveBtnClick()}>
                        Save
                    </Button>
                </DialogActions>
            </Dialog>
        </>
    );
}
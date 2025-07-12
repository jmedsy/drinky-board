import PeopleIcon from '@mui/icons-material/People';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import * as React from 'react';

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

export default function SidebarDIButton() {
    const [openDialog, setOpenDialog] = React.useState(false);
    const [profiles, setProfiles] = React.useState<TypingProfile[]>(() => {
        // Only access localStorage in the browser
        if (typeof window !== 'undefined') {
            const saved = localStorage.getItem('typingProfiles');
            return saved ? JSON.parse(saved) : [];
        }
        return [];
    });

    // Save profiles to localStorage whenever they change
    React.useEffect(() => {
        if (typeof window !== 'undefined') {
            localStorage.setItem('typingProfiles', JSON.stringify(profiles));
        }
    }, [profiles]);

    const handleButtonClick = () => {
        setOpenDialog(true);
    }

    const loadProfilesFromFile = (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files?.[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const loadedProfiles = JSON.parse(e.target?.result as string) as TypingProfile[];
                setProfiles(loadedProfiles);
            } catch (error) {
                console.error('Error loading profiles:', error);
                alert('Invalid profiles file');
            }
        };
        reader.readAsText(file);
    };

    return (
        <>
            <ListItemButton onClick={handleButtonClick}>
                <ListItemIcon>
                    <PeopleIcon />
                </ListItemIcon>
                <ListItemText primary='Typing Profiles' />
            </ListItemButton>

            <Dialog
                open={openDialog}
                onClose={() => setOpenDialog(false)}
                aria-labelledby="alert-dialog-title"
                aria-describedby="alert-dialog-description"
                maxWidth="md"
                fullWidth
            >
                <DialogTitle id="alert-dialog-title">
                    Typing Profiles
                </DialogTitle>
                <DialogContent>
                    <Box sx={{ display: 'flex', gap: 2 }}>
                        <Box sx={{ flex: '0 0 30%' }}>
                            <Box sx={{ mt: 2, height: '100%', display: 'flex', flexDirection: 'column' }}>
                                <Button
                                    variant="outlined"
                                    sx={{
                                        flex: 1,
                                        height: '100%',
                                        minHeight: '200px',
                                        position: 'relative',
                                        overflow: 'hidden',
                                        '&::before': {
                                            content: '""',
                                            position: 'absolute',
                                            top: '50%',
                                            left: '50%',
                                            transform: 'translate(-50%, -50%)',
                                            width: '80px',
                                            height: '80px',
                                            backgroundImage: 'url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'%23e0e0e0\'%3E%3Cpath d=\'M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z\'/%3E%3C/svg%3E")',
                                            backgroundSize: 'contain',
                                            backgroundRepeat: 'no-repeat',
                                            backgroundPosition: 'center',
                                            opacity: 0.3,
                                            pointerEvents: 'none'
                                        }
                                    }}
                                >
                                    Add Profile
                                </Button>
                            </Box>
                        </Box>
                        <Box sx={{ flex: 1, display: 'flex', alignItems: 'center' }}>
                            <DialogContentText id="alert-dialog-description">
                                Create typing profiles for customizing things like <strong><em>average wpm</em></strong>, <strong><em>average key hold time</em></strong>, etc.
                            </DialogContentText>
                        </Box>
                    </Box>
                </DialogContent>
                <DialogActions>
                    <Button
                        onClick={() => {
                            document.getElementById('load-profiles-button')?.click();
                        }}
                        sx={{ ml: 1 }}
                    >
                        Import Profiles
                    </Button>
                    <input
                        accept=".json"
                        style={{ display: 'none' }}
                        id="load-profiles-button"
                        type="file"
                        onChange={loadProfilesFromFile}
                    />
                    <Box sx={{ flex: 1 }} />
                    <Button onClick={() => setOpenDialog(false)}>Back</Button>
                    <Button variant="contained" color="primary" disabled>
                        Save
                    </Button>
                </DialogActions>
            </Dialog>
        </>
    );
}
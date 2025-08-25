import AddIcon from '@mui/icons-material/Add';
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
import MenuItem from '@mui/material/MenuItem';
import Paper from '@mui/material/Paper';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import * as React from 'react';
import DraggableList from '../DraggableList';

const flaskUrl = process.env.NEXT_PUBLIC_FLASK_BASE_URL;

interface SequenceInterface {
    name: string;
    wpm: number;
    wpmVariation: number;
    keyDuration: number;
    keyDurationVariation: number;
    description?: string;
    created: string;
    isActive: boolean;
}

interface Sequence {
    filename: string;
    data: SequenceInterface;
}

export default function SidebarSequencesButton() {
    const [openDialog, setOpenDialog] = React.useState(false);
    const [saveBtnEnabled, setSaveBtnEnabled] = React.useState(false);
    const [sequences, setSequences] = React.useState<Sequence[]>([]);
    const [selectedSequence, setSelectedSequence] = React.useState<string | null>(null);
    const [isAddNewSelected, setIsAddNewSelected] = React.useState(false);
    const [formData, setFormData] = React.useState({
        name: '',
        wpm: 60,
        wpmVariation: 10,
        keyDuration: 100,
        keyDurationVariation: 20,
        description: '',
        isActive: false
    });
    const [dialogKey, setDialogKey] = React.useState(0);
    const [newAction, setNewAction] = React.useState<{
        type: string;
        duration?: string;
        key?: string;
        text?: string;
        modifiers?: string[];
        sequence?: string;
        filepath?: string;
    }>({ type: '' });

    const modifierOptions = ['Ctrl', 'Shift', 'Alt', 'Meta'];
    const keyOptions = [
        'A', 'B', 'C', '1', '2', '3', 'Enter', 'Space', 'Tab', 'Escape', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'
    ];

    /* API function */
    const postSequence = async () => {
        const sequenceData = {
            name: formData.name,
            wpm: formData.wpm,
            wpmVariation: formData.wpmVariation,
            keyDuration: formData.keyDuration,
            keyDurationVariation: formData.keyDurationVariation,
            description: formData.description,
            isActive: formData.isActive
        };

        const res = await fetch(`${flaskUrl}/sequences/add`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(sequenceData)
        });

        return res;
    }

    /* API function */
    const putSequence = async (filename: string) => {
        const sequenceData = {
            name: formData.name,
            wpm: formData.wpm,
            wpmVariation: formData.wpmVariation,
            keyDuration: formData.keyDuration,
            keyDurationVariation: formData.keyDurationVariation,
            description: formData.description,
            isActive: formData.isActive
        };

        const res = await fetch(`${flaskUrl}/sequences/edit/${filename}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(sequenceData)
        });

        return res;
    }

    /* API function */
    const getAllSequences = async () => {
        const res = await fetch(`${flaskUrl}/sequences/get_all`);
        return res;
    }

    /* API function */
    const deleteSequence = async (filename: string) => {
        const res = await fetch(`${flaskUrl}/sequences/delete/${filename}`, {
            method: 'DELETE'
        });
        return res;
    }

    /* API Function */
    const deactivateExcept = async (filename: string) => {
        const res = await fetch(`${flaskUrl}/sequences/deactivateExcept/${filename}`, {
            method: 'PUT',
        });
        return res;
    }

    /* API function */
    const updateSequenceOrder = async (sequencesArg: string[]) => {

        const res = await fetch(`${flaskUrl}/preferences/update_sequence_order`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(sequencesArg)
        });
        return res;
    }

    const handleButtonClick = () => {
        refreshSequences();
        setOpenDialog(true);
    }

    const handleAddNewClick = () => {
        setSaveBtnEnabled(true);
        setSelectedSequence(null);
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
    }

    const handleSequenceSelect = (sequence: Sequence) => {
        setSelectedSequence(sequence.filename);
        setSaveBtnEnabled(true);
        setIsAddNewSelected(false);
        setFormData({
            ...sequence.data,
            description: sequence.data.description || ''
        });
    }

    const resetToInitialState = () => {
        setSelectedSequence(null);
        setIsAddNewSelected(false);
        setSaveBtnEnabled(false);
        setFormData({
            name: '',
            wpm: 60,
            wpmVariation: 10,
            keyDuration: 100,
            keyDurationVariation: 20,
            description: '',
            isActive: false
        });
    }

    const handleSaveBtnClick = async () => {
        setSaveBtnEnabled(false);

        try {
            const res = selectedSequence ? await putSequence(selectedSequence) : await postSequence();
            const data = await res.json();

            if (!data.success) {
                throw new Error(data.message);
            } else {
                console.log(`Sequence ${selectedSequence ? 'edited' : 'saved'} successfully:`, data);
            }

            // Only deactivate others if this sequence is being set as active
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
            refreshSequences();
            resetToInitialState();
        } catch (err) {
            console.error('API call failed:', err);
            // Re-enable save button on error
            setSaveBtnEnabled(true);
        }
    }

    const deleteHandler = async (filename: string) => {
        try {
            const res = await deleteSequence(filename);
            const data = await res.json();

            if (!data.success) {
                throw new Error(data.message);
            } else {
                console.log('Sequence deleted successfully:', data);
                refreshSequences();
            }
        } catch (err) {
            console.error('Delete API call failed:', err);
        }
    }

    const refreshSequences = async () => {
        setDialogKey(k => k + 1); // Force total rerender to play nice with SortableJS
        try {
            const res = await getAllSequences();
            const data = await res.json();

            if (!data.success) {
                throw new Error(data.message);
            } else {
                const sequenceList = data.sequences.map((s: Sequence) => s);
                setSequences(sequenceList);
                setDialogKey(k => k + 1); // Force total rerender to play nice with SortableJS
                resetToInitialState();
            }
        } catch (err) {
            console.error('API call failed:', err);
        }
    }

    const handleReorder = async (oldIndex: number, newIndex: number) => {
        const oldSequences = [...sequences];
        const item = oldSequences.splice(oldIndex, 1)[0];
        oldSequences.splice(newIndex, 0, item);
        const res = await updateSequenceOrder(oldSequences.map(seq => seq.filename));
        const data = await res.json();

        if (data.success) {
            console.log(data);
            setSequences(oldSequences);
            // setDialogKey(k => k + 1); // Force total rerender to play nice with SortableJS
            refreshSequences(); // Redundant, but makes absolutely sure UI is in sync
        } else {
            console.error('Error handling list reorder');
        }
    };

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
                <DialogContent key={dialogKey}>
                    <Box sx={{ display: 'flex', gap: 2 }}>
                        <Box sx={{ flex: '0 0 30%' }}>
                            <Box sx={{ mt: 2, display: 'flex', flexDirection: 'column' }}>
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
                                <Box sx={{
                                    height: '400px',
                                    overflowY: 'auto',
                                    border: '1px solid #e0e0e0',
                                    borderRadius: 1,
                                    p: 1,
                                    backgroundColor: '#fafafa'
                                }}>
                                    <DraggableList
                                        onReorder={handleReorder}
                                        items={sequences.map((s, index) => (
                                            <Paper
                                                key={index}
                                                sx={{
                                                    height: '60px',
                                                    mb: 1,
                                                    p: 2,
                                                    backgroundColor: selectedSequence === s.filename ? '#e3f2fd' : '#fefefe',
                                                    border: selectedSequence === s.filename ? '1px solid #2196f3' : '1px solid #e8e8e8',
                                                    display: 'flex',
                                                    flexDirection: 'column',
                                                    justifyContent: 'space-between',
                                                    position: 'relative',
                                                    cursor: 'pointer',
                                                    userSelect: 'none',
                                                    '&:hover': {
                                                        backgroundColor: selectedSequence === s.filename ? '#e3f2fd' : '#f5f5f5'
                                                    }
                                                }}
                                                onClick={() => handleSequenceSelect(s)}
                                            >
                                                <Box sx={{
                                                    position: 'absolute',
                                                    top: 4,
                                                    right: 4,
                                                    display: 'flex',
                                                    gap: 0.5
                                                }}>
                                                    <IconButton
                                                        size="small"
                                                        sx={{ p: 0.5 }}
                                                        onClick={(event) => {
                                                            event?.stopPropagation();
                                                            deleteHandler(s.filename);
                                                        }
                                                        }>
                                                        <DeleteIcon fontSize="small" />
                                                    </IconButton>
                                                </Box>
                                                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                                    <Typography variant="body2" noWrap sx={{ fontWeight: 'bold', maxWidth: '50%' }}>
                                                        {s.data.name}
                                                    </Typography>
                                                    <Typography variant="caption" sx={{ color: s.data.isActive ? 'green' : 'gray', mr: 3 }}>
                                                        {s.data.isActive ? 'Active' : 'Inactive'}
                                                    </Typography>
                                                </Box>
                                                <Box sx={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.7rem', color: '#666' }}>
                                                    <span>WPM: {s.data.wpm}±{s.data.wpmVariation}</span>
                                                    <span>Duration: {s.data.keyDuration}±{s.data.keyDurationVariation}ms</span>
                                                </Box>
                                            </Paper>
                                        ))}
                                    />
                                </Box>
                            </Box>
                        </Box>
                        <Box sx={{ flex: 1, display: 'flex', alignItems: 'center' }}>
                            <Box sx={{ width: '100%', p: 2 }}>
                                <Typography variant="h6" sx={{ mb: 2 }}>
                                    {selectedSequence ? 'Edit Sequence' : 'New Sequence'}
                                </Typography>
                                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                                    <TextField
                                        label="Sequence Name"
                                        value={formData.name}
                                        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                                        size="small"
                                        disabled={!saveBtnEnabled}
                                    />
                                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mt: 1 }}>
                                        <TextField
                                            select
                                            label="Action"
                                            value={newAction.type}
                                            onChange={e => setNewAction({ ...newAction, type: e.target.value })}
                                            size="small"
                                            sx={{ minWidth: 110 }}
                                            disabled={!saveBtnEnabled}
                                        >
                                            <MenuItem value=""><em>None</em></MenuItem>
                                            <MenuItem value="delay">Delay</MenuItem>
                                            <MenuItem value="keypress">Keypress</MenuItem>
                                            <MenuItem value="text">Text</MenuItem>
                                            <MenuItem value="sequence">Sequence</MenuItem>
                                            <MenuItem value="file">File</MenuItem>
                                        </TextField>
                                        {newAction?.type === 'delay' && (
                                            <TextField
                                                label="Duration (ms)"
                                                type="number"
                                                value={newAction.duration || ''}
                                                onChange={e => setNewAction({ ...newAction, duration: e.target.value })}
                                                size="small"
                                                sx={{ minWidth: 80 }}
                                            />
                                        )}
                                        {newAction?.type === 'keypress' && (
                                            <>
                                                <TextField
                                                    select
                                                    label="Key"
                                                    value={newAction.key || ''}
                                                    onChange={e => setNewAction({ ...newAction, key: e.target.value })}
                                                    size="small"
                                                    sx={{ minWidth: 80 }}
                                                    disabled={!saveBtnEnabled}
                                                >
                                                    <MenuItem value=""><em>None</em></MenuItem>
                                                    {keyOptions.map(opt => (
                                                        <MenuItem key={opt} value={opt}>{opt}</MenuItem>
                                                    ))}
                                                </TextField>
                                                {[0, 1, 2].map((idx) => (
                                                    <TextField
                                                        key={idx}
                                                        select
                                                        label={`Mod ${idx + 1}`}
                                                        value={newAction.modifiers?.[idx] || ''}
                                                        onChange={e => {
                                                            const value = e.target.value;
                                                            let newModifiers = (newAction.modifiers || []).slice();
                                                            newModifiers[idx] = value;
                                                            // Remove duplicates
                                                            newModifiers = newModifiers.filter((mod, i, arr) => mod && arr.indexOf(mod) === i);
                                                            setNewAction({ ...newAction, modifiers: newModifiers });
                                                        }}
                                                        size="small"
                                                        sx={{ minWidth: 90 }}
                                                        disabled={!saveBtnEnabled}
                                                    >
                                                        <MenuItem value=""><em>None</em></MenuItem>
                                                        {modifierOptions.filter(opt => !(newAction.modifiers || []).includes(opt) || (newAction.modifiers?.[idx] === opt)).map(opt => (
                                                            <MenuItem key={opt} value={opt}>{opt}</MenuItem>
                                                        ))}
                                                    </TextField>
                                                ))}
                                            </>
                                        )}
                                        {newAction?.type === 'text' && (
                                            <TextField
                                                label="Text"
                                                value={newAction.text || ''}
                                                onChange={e => setNewAction({ ...newAction, text: e.target.value })}
                                                size="small"
                                                sx={{ minWidth: 80 }}
                                            />
                                        )}
                                        {newAction?.type === 'sequence' && (
                                            <>
                                                <TextField
                                                    select
                                                    label="Sequence"
                                                    value={newAction.key || ''}
                                                    onChange={e => setNewAction({ ...newAction, key: e.target.value })}
                                                    size="small"
                                                    sx={{ minWidth: 120 }}
                                                    disabled={!saveBtnEnabled}
                                                >
                                                    <MenuItem value=""><em>None</em></MenuItem>
                                                </TextField>
                                            </>
                                        )}
                                        <IconButton
                                            size="small"
                                            color="primary"
                                            disabled={!newAction?.type}
                                            onClick={() => {
                                                // Dummy add action logic
                                                setNewAction({ type: '' });
                                            }}
                                            aria-label="Add Action"
                                            sx={{ alignSelf: 'center', mt: '7px' }}
                                        >
                                            <AddIcon />
                                        </IconButton>
                                    </Box>
                                    {/* You can add more fields or controls here as needed */}
                                    <Box sx={{
                                        height: '200px',
                                        overflowY: 'auto',
                                        border: '1px solid #e0e0e0',
                                        borderRadius: 1,
                                        p: 1,
                                        backgroundColor: '#fafafa'
                                    }}>
                                        <DraggableList
                                            // onReorder={handleReorder}
                                            items={[
                                                <Paper key={1} sx={{ height: '36px', mb: 1, p: 1, display: 'flex', alignItems: 'center', minWidth: 0, borderLeft: '6px solid #1976d2', background: '#e3f2fd' }}>
                                                    <Typography variant="body2" noWrap sx={{ fontWeight: 'bold', maxWidth: '70%' }}>
                                                        Delay: 500ms
                                                    </Typography>
                                                </Paper>,
                                                <Paper key={2} sx={{ height: '36px', mb: 1, p: 1, display: 'flex', alignItems: 'center', minWidth: 0, borderLeft: '6px solid #388e3c', background: '#e8f5e9' }}>
                                                    <Typography variant="body2" noWrap sx={{ fontWeight: 'bold', maxWidth: '70%' }}>
                                                        Keypress: A + Ctrl
                                                    </Typography>
                                                </Paper>,
                                                <Paper key={3} sx={{ height: '36px', mb: 1, p: 1, display: 'flex', alignItems: 'center', minWidth: 0, borderLeft: '6px solid #f57c00', background: '#fff3e0' }}>
                                                    <Typography variant="body2" noWrap sx={{ fontWeight: 'bold', maxWidth: '70%' }}>
                                                        Text: &quot;Hello!&quot;
                                                    </Typography>
                                                </Paper>,
                                                <Paper key={4} sx={{ height: '36px', mb: 1, p: 1, display: 'flex', alignItems: 'center', minWidth: 0, borderLeft: '6px solid #8e24aa', background: '#f3e5f5' }}>
                                                    <Typography variant="body2" noWrap sx={{ fontWeight: 'bold', maxWidth: '70%' }}>
                                                        Sequence: MySequence
                                                    </Typography>
                                                </Paper>,
                                                <Paper key={5} sx={{ height: '36px', mb: 1, p: 1, display: 'flex', alignItems: 'center', minWidth: 0, borderLeft: '6px solid #fbc02d', background: '#fffde7' }}>
                                                    <Typography variant="body2" noWrap sx={{ fontWeight: 'bold', maxWidth: '70%' }}>
                                                        File: myfile.txt
                                                    </Typography>
                                                </Paper>
                                            ]}
                                        />
                                    </Box>
                                    <TextField
                                        label="Description (optional)"
                                        value={formData.description}
                                        onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                                        size="small"
                                        multiline
                                        rows={2}
                                        disabled={!saveBtnEnabled}
                                        sx={{ mt: 2 }}
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
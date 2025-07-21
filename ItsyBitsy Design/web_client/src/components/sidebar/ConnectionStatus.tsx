import FiberManualRecordIcon from '@mui/icons-material/FiberManualRecord';
import { Box, Chip, CircularProgress, ListItemButton, ListItemIcon, ListItemText } from '@mui/material';
import React, { useEffect, useState } from 'react';

const flaskUrl = process.env.NEXT_PUBLIC_FLASK_BASE_URL;

interface ConnectionStatusData {
    connected: boolean;
    status: 'connected' | 'disconnected' | 'unresponsive';
    message: string;
    port: string | null;
    last_heartbeat: number | null;
}

const ConnectionStatus: React.FC = () => {
    const [status, setStatus] = useState<ConnectionStatusData | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    const fetchStatus = async () => {
        try {
            const response = await fetch(`${flaskUrl}/connection_status`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            setStatus(data);
            setError(null);
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to fetch status');
            setStatus(null);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchStatus();

        const pollInterval = Number(process.env.NEXT_PUBLIC_DRINKY_STATUS_POLL_MS) || 500;
        const interval = setInterval(fetchStatus, pollInterval);

        return () => clearInterval(interval);
    }, []);

    const getStatusText = () => {
        if (loading) return 'Checking connection...';
        if (error) return 'Connection error';
        if (!status) return 'Unknown status';

        switch (status.status) {
            case 'connected':
                return 'Connected';
            case 'disconnected':
                return 'Disconnected';
            case 'unresponsive':
                return 'Unresponsive';
            default:
                return 'Unknown';
        }
    };

    const getStatusColor = () => {
        if (loading || error) return 'default';
        if (status?.connected) return 'success';
        return 'error';
    };

    const getIconColor = () => {
        if (loading) return 'action.disabled';
        if (error || !status?.connected) return 'error.main';
        return 'success.main';
    };

    return (
        <Box sx={{
            display: 'flex',
            alignItems: 'center',
            borderBottom: 1,
            borderColor: 'divider',
            userSelect: 'none',
        }}>
            <ListItemButton
                disabled
                sx={{
                    flex: 1,
                    '&:hover': {
                        backgroundColor: 'transparent'
                    },
                    '&.Mui-disabled': {
                        opacity: 1,
                        color: 'inherit'
                    },
                    userSelect: 'none',
                }}
            >
                <ListItemIcon>
                    {loading ? (
                        <CircularProgress size={20} />
                    ) : (
                        <FiberManualRecordIcon
                            sx={{
                                color: getIconColor()
                            }}
                        />
                    )}
                </ListItemIcon>
                <ListItemText primary="Device Status" />
            </ListItemButton>
            <Box sx={{ paddingRight: 2 }}>
                <Chip
                    label={getStatusText()}
                    color={getStatusColor()}
                    size="small"
                    variant="outlined"
                />
            </Box>
        </Box>
    );
};

export default ConnectionStatus; 
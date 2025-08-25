import FiberManualRecordIcon from '@mui/icons-material/FiberManualRecord';
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { keyframes } from '@mui/system';

const pulse = keyframes`
0%, 100% {
    transform: scale(1);
    opacity: 1;
}
50% {
    transform: scale(1.5);
    opacity: 0.6;
}
`;

interface DIBackdropProps {
    open: boolean;
    onClick: () => void;
}

export default function DIBackdrop({ open, onClick }: DIBackdropProps) {
    return (
        <Backdrop
            sx={{
                backgroundColor: 'rgba(0, 0, 0, 0.93)',
                zIndex: 9999,
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                position: 'fixed',
                top: 0,
                left: 0,
                right: 0,
                bottom: 0,
            }}
            open={open}
            onClick={onClick}
        >
            {open && (
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                    <FiberManualRecordIcon
                        fontSize="large"
                        color='error'
                        sx={{ animation: `${pulse} 1s infinite` }}
                    />
                    <Typography variant="subtitle2" color="white" sx={{ userSelect: 'none' }}>
                        Click anywhere to exit Direct Input mode
                    </Typography>
                </Box>
            )}
        </Backdrop>
    );
}

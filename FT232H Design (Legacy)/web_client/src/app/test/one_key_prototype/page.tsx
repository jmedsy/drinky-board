'use client';

import { Box, Button, Typography } from '@mui/material';

const PlaygroundPage = () => {

    const handleSubmit = async () => {
        try {
            const response = await fetch('http://localhost:8000/flask_api/one_key/trigger_once', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    text: 'Hello, world!'
                })
            })

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
        } catch (error) {
            console.error('Error submitting text:', error);
            alert('Failed to send request to backend. Is it running?');
        }
    };

    return (
        <Box>
            <Typography variant="h3" gutterBottom>One-Key Prototype</Typography>
            <Button onClick={handleSubmit} >Type Backtick Once</Button>
        </Box>
    );
}

export default PlaygroundPage;
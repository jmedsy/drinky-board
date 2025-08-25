const flaskUrl = process.env.NEXT_PUBLIC_FLASK_BASE_URL;

export const fetchDeviceStatus = async () => {
    const res = await fetch(`${flaskUrl}/connection_status`);

    return res;
}

export const listen = async (code: string, data: unknown[], eventType: string = 'keydown') => {
    const res = await fetch(`${flaskUrl}/direct_input/listen`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            code: code,
            data: data,
            type: eventType
        })
    });

    return res;
}
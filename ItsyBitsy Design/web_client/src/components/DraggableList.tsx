import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import * as React from 'react';
import Sortable from 'sortablejs';

interface DraggableListProps {
    height?: string;
}

// Individual draggable item component
function DraggableItemComponent({
    children,
    isDragging
}: {
    children: React.ReactNode;
    isDragging: boolean;
}) {
    return (
        <Paper
            sx={{
                p: 2,
                mb: 1,
                backgroundColor: '#ffffff',
                border: '1px solid #e8e8e8',
                borderRadius: 1,
                cursor: 'grab',
                '&:active': { cursor: 'grabbing' },
                '&:hover': isDragging ? {} : { backgroundColor: '#f5f5f5' },
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                minHeight: '60px'
            }}
        >
            {children}
        </Paper>
    );
}

export default function DraggableList({
    height = '300px'
}: DraggableListProps) {
    // Hardcoded dummy components
    const [items] = React.useState<React.ReactNode[]>([
        <Box key="1" sx={{ p: 2, backgroundColor: '#e3f2fd', borderRadius: 1, textAlign: 'center' }}>
            <Typography variant="h6">Box 1</Typography>
            <Typography variant="body2">This is the first box</Typography>
        </Box>,
        <Box key="2" sx={{ p: 2, backgroundColor: '#f3e5f5', borderRadius: 1, textAlign: 'center' }}>
            <Typography variant="h6">Box 2</Typography>
            <Typography variant="body2">This is the second box</Typography>
        </Box>,
        <Box key="3" sx={{ p: 2, backgroundColor: '#e8f5e8', borderRadius: 1, textAlign: 'center' }}>
            <Typography variant="h6">Box 3</Typography>
            <Typography variant="body2">This is the third box</Typography>
        </Box>,
        <Box key="4" sx={{ p: 2, backgroundColor: '#fff3e0', borderRadius: 1, textAlign: 'center' }}>
            <Typography variant="h6">Box 4</Typography>
            <Typography variant="body2">This is the fourth box</Typography>
        </Box>,
        <Box key="5" sx={{ p: 2, backgroundColor: '#fce4ec', borderRadius: 1, textAlign: 'center' }}>
            <Typography variant="h6">Box 5</Typography>
            <Typography variant="body2">This is the fifth box</Typography>
        </Box>,
        <Box key="6" sx={{ p: 2, backgroundColor: '#e0f2f1', borderRadius: 1, textAlign: 'center' }}>
            <Typography variant="h6">Box 6</Typography>
            <Typography variant="body2">This is the sixth box</Typography>
        </Box>
    ]);

    const [isDragging, setIsDragging] = React.useState(false);
    const containerRef = React.useRef<HTMLDivElement>(null);
    const sortableRef = React.useRef<Sortable | null>(null);

    // Initialize SortableJS
    React.useEffect(() => {
        if (containerRef.current && !sortableRef.current) {
            sortableRef.current = Sortable.create(containerRef.current, {
                animation: 150,
                ghostClass: 'sortable-ghost',
                chosenClass: 'sortable-chosen',
                dragClass: 'sortable-drag',
                onStart: (evt) => {
                    evt.item.style.visibility = 'hidden';
                    setIsDragging(true);
                },
                onEnd: (evt) => {
                    evt.item.style.visibility = 'visible';
                    setIsDragging(false);
                }
            });
        }

        return () => {
            if (sortableRef.current) {
                sortableRef.current.destroy();
                sortableRef.current = null;
            }
        };
    }, []);

    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
            <Box sx={{
                height,
                overflowY: 'auto',
                overflowX: 'hidden',
                border: '1px solid #e0e0e0',
                borderRadius: 1,
                p: 1,
                backgroundColor: '#fafafa'
            }}>
                <div ref={containerRef}>
                    {items.map((item, index) => (
                        <DraggableItemComponent
                            key={index}
                            isDragging={isDragging}
                        >
                            {item}
                        </DraggableItemComponent>
                    ))}
                </div>
            </Box>

            <style jsx>{`
                .sortable-ghost {
                    opacity: 0.3;
                    background: #e0e0e0;
                    border: 2px dashed #999;
                }
                .sortable-chosen {
                    background: #e3f2fd;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }
                .sortable-drag {
                    opacity: 1;
                    transform: rotate(2deg);
                    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                }
            `}</style>
        </Box>
    );
} 
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import * as React from 'react';
import Sortable from 'sortablejs';

export interface DraggableItem {
    id: string;
    type: string;
    description: string;
}

interface DraggableListProps {
    height?: string;
    title?: string;
}

// Individual draggable item component
function DraggableItemComponent({
    item,
    isDragging
}: {
    item: DraggableItem;
    isDragging: boolean;
}) {
    return (
        <Paper
            data-id={item.id}
            sx={{
                p: 1,
                mb: 0.5,
                backgroundColor: '#ffffff',
                border: '1px solid #e8e8e8',
                borderRadius: 1,
                cursor: 'grab',
                '&:active': { cursor: 'grabbing' },
                '&:hover': isDragging ? {} : { backgroundColor: '#f5f5f5' },
                display: 'flex',
                alignItems: 'center',
                gap: 1
            }}
        >
            <Box sx={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                width: '100%'
            }}>
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                    <Typography variant="body2" sx={{ fontWeight: 'bold' }}>
                        {item.type}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        {item.description}
                    </Typography>
                </Box>
            </Box>
        </Paper>
    );
}

export default function DraggableList({
    height = '300px',
    title = 'Items (drag to reorder)'
}: DraggableListProps) {
    // Hardcoded dummy data
    const [items] = React.useState<DraggableItem[]>([
        { id: '1', type: 'Type Text', description: 'Hello World' },
        { id: '2', type: 'Delay', description: '500ms' },
        { id: '3', type: 'Keyboard Shortcut', description: 'Ctrl+C' },
        { id: '4', type: 'Type File', description: 'config.txt' },
        { id: '5', type: 'Delay', description: '1000ms' },
        { id: '6', type: 'Type Text', description: 'Goodbye' }
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
            {title && (
                <Typography variant="subtitle2" sx={{ mb: 1 }}>
                    {title}
                </Typography>
            )}

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
                    {items.map((item) => (
                        <DraggableItemComponent
                            key={item.id}
                            item={item}
                            isDragging={isDragging}
                        />
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
                [data-id] {
                    user-select: none;
                    -webkit-user-select: none;
                    -moz-user-select: none;
                    -ms-user-select: none;
                }
            `}</style>
        </Box>
    );
} 
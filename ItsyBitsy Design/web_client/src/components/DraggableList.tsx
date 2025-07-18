import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import * as React from 'react';
import Sortable from 'sortablejs';

interface DraggableListProps {
    height?: string;
    items: React.ReactNode[];
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
    height = '300px',
    items
}: DraggableListProps) {
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
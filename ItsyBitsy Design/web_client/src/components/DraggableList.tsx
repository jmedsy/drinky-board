import Box from '@mui/material/Box';
import * as React from 'react';
import Sortable from 'sortablejs';

interface DraggableListProps<T> {
    items: T[];
    onReorder?: (items: T[]) => void;
    height?: string;
    itemTemplate: (item: T, index: number) => React.ReactNode;
}

export default function DraggableList<T>({
    items,
    onReorder,
    height = '300px',
    itemTemplate
}: DraggableListProps<T>) {
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
                },
                onEnd: (evt) => {
                    evt.item.style.visibility = 'visible';
                    const { oldIndex, newIndex } = evt;
                    if (oldIndex !== newIndex && oldIndex !== undefined && newIndex !== undefined && onReorder) {
                        const newItems = [...items];
                        const [movedItem] = newItems.splice(oldIndex, 1);
                        newItems.splice(newIndex, 0, movedItem);
                        onReorder(newItems);
                    }
                }
            });
        }

        return () => {
            if (sortableRef.current) {
                sortableRef.current.destroy();
                sortableRef.current = null;
            }
        };
    }, [items, onReorder]);

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
                        <div key={index} data-id={index}>
                            {itemTemplate(item, index)}
                        </div>
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
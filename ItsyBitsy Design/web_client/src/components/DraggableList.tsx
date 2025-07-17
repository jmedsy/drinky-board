import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import * as React from 'react';
import Sortable from 'sortablejs';

export interface DraggableItem {
    id: string;
    type: string;
    description: string;
}

interface DraggableListProps {
    items?: DraggableItem[];
    onItemsChange?: (items: DraggableItem[]) => void;
    height?: string;
    title?: string;
    itemTemplate: (item: DraggableItem, onRemove: () => void, isDragging: boolean) => React.ReactNode;
}

// Individual draggable item component
function DraggableItemComponent({
    item,
    onRemove,
    isDragging,
    itemTemplate
}: {
    item: DraggableItem;
    onRemove: () => void;
    isDragging: boolean;
    itemTemplate: (item: DraggableItem, onRemove: () => void, isDragging: boolean) => React.ReactNode;
}) {
    return (
        <div data-id={item.id}>
            {itemTemplate(item, onRemove, isDragging)}
        </div>
    );
}

export default function DraggableList({
    items: initialItems,
    onItemsChange,
    height = '300px',
    title = 'Items (drag to reorder)',
    itemTemplate
}: DraggableListProps) {
    const [items, setItems] = React.useState(initialItems || []);
    const [isDragging, setIsDragging] = React.useState(false);
    const containerRef = React.useRef<HTMLDivElement>(null);
    const sortableRef = React.useRef<Sortable | null>(null);

    // Update internal state when props change
    React.useEffect(() => {
        if (initialItems) {
            setItems(initialItems);
        }
    }, [initialItems]);

    // Notify parent when items change
    React.useEffect(() => {
        if (onItemsChange) {
            onItemsChange(items);
        }
    }, [items, onItemsChange]);

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
                    const { oldIndex, newIndex } = evt;
                    if (oldIndex !== newIndex && oldIndex !== undefined && newIndex !== undefined) {
                        const newItems = [...items];
                        const [movedItem] = newItems.splice(oldIndex, 1);
                        newItems.splice(newIndex, 0, movedItem);
                        setItems(newItems);
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
    }, [items]);

    const removeItem = (id: string) => {
        const newItems = items.filter(item => item.id !== id);
        setItems(newItems);
    };

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
                            onRemove={() => removeItem(item.id)}
                            isDragging={isDragging}
                            itemTemplate={itemTemplate}
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
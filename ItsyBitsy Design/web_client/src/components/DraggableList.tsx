import DeleteIcon from '@mui/icons-material/Delete';
import Box from '@mui/material/Box';
// import Button from '@mui/material/Button';
import FormControl from '@mui/material/FormControl';
import IconButton from '@mui/material/IconButton';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Paper from '@mui/material/Paper';
import Select from '@mui/material/Select';
import Typography from '@mui/material/Typography';
import * as React from 'react';
import Sortable from 'sortablejs';
// import { v4 as uuidv4 } from 'uuid';

export interface DraggableItem {
    id: string;
    type: string;
    description: string;
}

interface DraggableListProps {
    items?: DraggableItem[];
    onItemsChange?: (items: DraggableItem[]) => void;
    onAddItem?: (type?: string) => void;
    height?: string;
    title?: string;
    addItemText?: string;
    actionTypes?: string[];
    itemTemplate?: (item: DraggableItem, onRemove: () => void, isDragging: boolean) => React.ReactNode;
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
    itemTemplate?: (item: DraggableItem, onRemove: () => void, isDragging: boolean) => React.ReactNode;
}) {
    // Use custom template if provided, otherwise use default
    if (itemTemplate) {
        return (
            <div data-id={item.id}>
                {itemTemplate(item, onRemove, isDragging)}
            </div>
        );
    }

    // Default template
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
                <IconButton
                    size="small"
                    onClick={(e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        onRemove();
                    }}
                    sx={{ p: 0.5 }}
                >
                    <DeleteIcon fontSize="small" />
                </IconButton>
            </Box>
        </Paper>
    );
}

export default function DraggableList({
    items: initialItems,
    onItemsChange,
    onAddItem,
    height = '300px',
    title = 'Items (drag to reorder)',
    // addItemText = '+ Add Item',
    actionTypes = ['Type Text', 'Delay', 'Keyboard Shortcut', 'Type File'],
    itemTemplate
}: DraggableListProps) {
    const [items, setItems] = React.useState(initialItems || []);
    const [selectedType, setSelectedType] = React.useState(actionTypes[0]);
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

    // Add item handler (if present)
    // const handleAddItem = (type?: string) => {
    //     const newAction: DraggableItem = {
    //         id: uuidv4(),
    //         type: type || 'New Action',
    //         description: 'Click to edit'
    //     };
    //     setItems([...items, newAction]);
    // };

    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
            {title && (
                <Typography variant="subtitle2" sx={{ mb: 1 }}>
                    {title}
                </Typography>
            )}

            {onAddItem && (
                <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
                    <FormControl size="small" sx={{ minWidth: 150 }}>
                        <InputLabel>Action Type</InputLabel>
                        <Select
                            value={selectedType}
                            label="Action Type"
                            onChange={(e) => setSelectedType(e.target.value)}
                        >
                            {actionTypes.map((type) => (
                                <MenuItem key={type} value={type}>
                                    {type}
                                </MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                    {/* <Button
                        variant="outlined"
                        size="small"
                        onClick={() => handleAddItem(selectedType)}
                    >
                        {addItemText}
                    </Button> */}
                </Box>
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
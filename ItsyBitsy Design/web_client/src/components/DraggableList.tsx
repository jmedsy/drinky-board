import * as React from 'react';
import Sortable from 'sortablejs';

interface DraggableListProps {
    items: React.ReactNode[];
    onReorder?: (oldIndex: number, newIndex: number) => void;
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
        <div style={{
            cursor: 'grab',
            opacity: isDragging ? 0.5 : 1
        }}>
            {children}
        </div>
    );
}

export default function DraggableList({
    items,
    onReorder
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
                    if (onReorder && evt.oldIndex !== undefined && evt.newIndex !== undefined) {
                        onReorder(evt.oldIndex, evt.newIndex);
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
    }, [onReorder]);

    return (
        <div ref={containerRef} style={{ height: '100%', overflowY: 'auto' }}>
            {items.map((item, index) => (
                <DraggableItemComponent
                    key={index}
                    isDragging={isDragging}
                >
                    {item}
                </DraggableItemComponent>
            ))}
        </div>
    );
} 
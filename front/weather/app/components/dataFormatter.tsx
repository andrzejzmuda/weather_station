export function formatTimestamp(timestamp: string): string {
    const date = new Date(timestamp);
    return new Intl.DateTimeFormat('pl-PL', {
        dateStyle: 'long',
        timeStyle: 'short'
    }).format(date)
}


export function formatTimestampShort(timestamp: string): string {
    const date = new Date(timestamp);
    return new Intl.DateTimeFormat('pl-PL', {
        dateStyle: 'short',
        timeStyle: 'short'
    }).format(date)
}


export function roundToOneDecimal(value: number): number {
    const rounded = Number(value.toFixed(1));
    return rounded === -0 ? 0 : rounded;
}


export function extractTime(timestamp: string): string {
    return new Date(timestamp).toLocaleTimeString('pl-PL', {
        hour: '2-digit',
        minute: '2-digit'
    });
}


export function extractDate(timestamp: string): string {
    const date = new Date(timestamp);
    return new Intl.DateTimeFormat('pl-PL', {
        dateStyle: 'short',
    }).format(date)
}
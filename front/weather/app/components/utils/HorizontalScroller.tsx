export function HorizontalScroller({ children }: { children: React.ReactNode }) {
  return (
    <div className="overflow-x-auto whitespace-nowrap pixel-panel p-4">
      <div className="inline-flex gap-4">{children}</div>
    </div>
  );
}

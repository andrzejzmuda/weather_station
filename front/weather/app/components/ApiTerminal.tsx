type LogEntry = {
  time: string;
  message: string;
};

{/* add live data*/}
export function ApiTerminal({ logs }: { logs: LogEntry[] }) {
  return (
    <div className="pixel-panel bg-black text-atari-green p-4 font-pixel text-xs max-h-64 overflow-y-auto">
      {logs.map((log, i) => (
        <p key={i} className="whitespace-pre">
          <span className="text-atari-yellow">{log.time}</span> {log.message}
        </p>
      ))}
    </div>
  );
}

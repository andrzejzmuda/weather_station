export function LoadingScreen() {
  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black text-atari-yellow font-pixel">
      <div className="text-center">
        <p className="mb-4">READY.</p>
        <p className="text-sm">
          RUN "WEATHER",8,1<span className="cursor">_</span>
        </p>
      </div>
    </div>
  );
}
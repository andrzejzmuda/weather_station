type Tile = {
  x: number;
  y: number;
  type: "sun" | "cloud" | "rain";
};

const COLORS: Record<Tile["type"], string> = {
  sun: "bg-atari-yellow",
  cloud: "bg-atari-cyan",
  rain: "bg-atari-blue",
};

export function WeatherMap({ tiles }: { tiles: Tile[] }) {
  return (
    <div className="pixel-panel inline-block">
      <div className="grid grid-cols-8 grid-rows-8">
        {tiles.map((t, i) => (
          <div
            key={i}
            className={`${COLORS[t.type]} w-4 h-4 border border-black`}
          />
        ))}
      </div>
    </div>
  );
}

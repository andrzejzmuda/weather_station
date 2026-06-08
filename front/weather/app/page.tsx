import fetchWeather from "./components/queries/fetchWeather";

export default async function Home() {
  const current = await fetchWeather({ url: "currentweather/" });

  return (
    <div className="flex flex-col items-center gap-6 py-10">
      

      <div className="pixel-panel p-4 flex gap-4 overflow-x-auto whitespace-nowrap">
        {current.map((c: any) => (
          <a
            key={c.geo_city}
            href={`/${encodeURIComponent(c.geo_id)}`}
            className="pixel-border bg-atari-black text-atari-cyan font-pixel px-4 py-2 inline-block"
          >
            {c.geo_city.toUpperCase()}
          </a>
        ))}
      </div>
    </div>
  );
}

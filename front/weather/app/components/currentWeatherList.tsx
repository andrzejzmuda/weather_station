import Image from "next/image";

import fetchWeather from "./queries/fetchWeather";
import MinutelyWeather from "./minutelyWeather";
import HourlyWeather from "./hourlyWeather";
import DailyWeather from "./dailyWeather";
import NavigationArrows from "./utils/NavArrows";
import { formatTimestamp, roundToOneDecimal } from "./utils/dataFormatter";
import { getWeatherIconByCode, getWeatherAnimation } from "./utils/weatherIconByCode";


export default async function CurrentWeatherList({ geo_id }: { geo_id: number }) {
  const current = await fetchWeather({ url: "currentweather/" });
  const allIds = current.map((c: any) => c.geo_id);
  const item = current.find((c: any) => c.geo_id === geo_id);

  if (!item) {
    return (
      <div className="text-atari-yellow font-pixel p-10">
        CITY NOT FOUND IN API
      </div>
    );
  }

  const icon = getWeatherIconByCode(item.weather_code);
  const anim = getWeatherAnimation(item.weather_code);

  return (
    <div className="flex flex-col items-center w-full py-10">
      
      <NavigationArrows currentId={geo_id} allIds={allIds} />

      <h2 className="text-2xl text-atari-yellow mb-6 font-pixel tracking-widest">
        {item.geo_city.toUpperCase()}
      </h2>

      {/* current panel */}
      <div className="pixel-border bg-atari-black text-atari-white p-6 mb-10 mx-auto inline-block text-center">

        <div className="flex items-center gap-4 mb-4">
          <Image
            src={icon}
            alt="weather icon"
            width={48}
            height={48}
            className={anim}/>
          <p className="text-xl text-atari-cyan font-pixel">
            {item.geo_city}
          </p>
        </div>
        <p className="text-xs text-atari-yellow mb-4 font-pixel">
          {formatTimestamp(item.weather_timestamp)}
        </p>
        <div className="space-y-2 font-pixel text-sm leading-relaxed">
          <p>TEMP: <span className="text-atari-cyan">{roundToOneDecimal(item.temperature_2m)}°C</span></p>
          <p>HUMIDITY: <span className="text-atari-yellow">{item.relative_humidity_2m}%</span></p>
          {item.rain > 0 ?
          <p>RAIN: <span className="text-atari-cyan">{roundToOneDecimal(item.rain)} mm</span></p>
          : null}
          {item.snowfall > 0 ?
          <p>SNOW: <span className="text-atari-cyan">{roundToOneDecimal(item.snowfall)} mm</span></p>
          : null}
          <p className="text-atari-yellow italic">{item.weather_description}</p>
        </div>
      </div>

      {/* forecast panels */}
      <MinutelyWeather geo_id={item.geo_id} />
      <HourlyWeather geo_id={item.geo_id} />
      <DailyWeather geo_id={item.geo_id} />
    </div>
  );
}
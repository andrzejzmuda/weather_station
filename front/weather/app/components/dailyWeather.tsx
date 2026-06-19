"use client";

import Image from "next/image";
import { useRef, useState, useEffect } from "react";
import fetchWeather from "./queries/fetchWeather";
import { extractDate, extractTime, roundToOneDecimal } from "./utils/dataFormatter";
import { getWeatherIconByCode, getWeatherAnimation } from "./utils/weatherIconByCode";

interface DailyWeather {
  url: string;
  date: string;
  sunrise: string;
  sunset: string;
  temperature_2m_mean: number;
  temperature_2m_min: number;
  temperature_2m_max: number;
  rain_sum: number;
  snowfall_sum: number;
  weather_code: number;
}


export default function DailyWeather({ geo_id }: { geo_id: number }) {

  const [dailyList, setDailyList] = useState<DailyWeather[]>([]);
  const url = "dailyweather/";
  const intervalMinute = 3600000 // 1 hour;
  const scrollRef = useRef<HTMLDivElement>(null);
  const [isDown, setIsDown] = useState(false);
  const [startX, setStartX] = useState(0);
  const [scrollLeft, setScrollLeft] = useState(0);

  const daily = () => {
      return fetchWeather({ url, geo_id });
    };
  
    useEffect(() => {
      if (!geo_id) return;
  
      async function load() {
        const data = await daily();
        setDailyList(data);
      }
      load();
      const interval = setInterval(() => {
        load();
      }, intervalMinute);
      return () => clearInterval(interval);
    }, [geo_id]);

  function handleMouseDown(e: React.MouseEvent) {
    setIsDown(true);
    setStartX(e.pageX - scrollRef.current!.offsetLeft);
    setScrollLeft(scrollRef.current!.scrollLeft);
  }

  function handleMouseLeave() {
    setIsDown(false);
  }

  function handleMouseUp() {
    setIsDown(false);
  }

  function handleMouseMove(e: React.MouseEvent) {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - scrollRef.current!.offsetLeft;
    const walk = (x - startX) * 1.2;
    scrollRef.current!.scrollLeft = scrollLeft - walk;
  }

  function handleTouchStart(e: React.TouchEvent) {
    setIsDown(true);
    setStartX(e.touches[0].pageX - scrollRef.current!.offsetLeft);
    setScrollLeft(scrollRef.current!.scrollLeft);
  }

  function handleTouchMove(e: React.TouchEvent) {
    if (!isDown) return;
    const x = e.touches[0].pageX - scrollRef.current!.offsetLeft;
    const walk = (x - startX) * 1.2;
    scrollRef.current!.scrollLeft = scrollLeft - walk;
  }

  function handleTouchEnd() {
    setIsDown(false);
  }

  return (
    <div className="w-full flex justify-center mt-6">
      <div
        className="pixel-panel w-full max-w-3xl p-3 overflow-hidden select-none cursor-grab active:cursor-grabbing"
        ref={scrollRef}
        onMouseDown={handleMouseDown}
        onMouseLeave={handleMouseLeave}
        onMouseUp={handleMouseUp}
        onMouseMove={handleMouseMove}
        onTouchStart={handleTouchStart}
        onTouchMove={handleTouchMove}
        onTouchEnd={handleTouchEnd}
      >
        <div className="inline-flex gap-3 w-max pr-3">
          {dailyList.map((d) => {
            const icon = getWeatherIconByCode(d.weather_code);
            const anim = getWeatherAnimation(d.weather_code);

            return (
              <div
                key={d.url}
                className="pixel-border bg-atari-black text-atari-white p-3 w-[150px] inline-block text-center"
              >
                <div className="flex items-center gap-2 mb-1">
                  <Image
                    src={icon}
                    alt="weather icon"
                    width={18}
                    height={18}
                    className={anim}
                  />
                  <p className="text-[9px] text-atari-yellow font-pixel truncate">
                    {extractDate(d.date)}
                  </p>
                </div>

                <div className="font-pixel text-[10px] space-y-1 leading-tight">
                    <p>SUNRISE: <span className="text-[9px] text-atari-cyan">{extractTime(d.sunrise)}</span></p>
                    <p>SUNSET: <span className="text-[9px] text-atari-cyan">{extractTime(d.sunset)}</span></p>
                    <p>TEMP MEAN: <span className="text-[9px] text-atari-cyan">{roundToOneDecimal(d.temperature_2m_mean)}°C</span></p>
                    <p>TEMP MIN: <span className="text-[9px] text-atari-cyan">{roundToOneDecimal(d.temperature_2m_min)}°C</span></p>
                    <p>TEMP MAX: <span className="text-[9px] text-atari-cyan">{roundToOneDecimal(d.temperature_2m_max)}°C</span></p>
                    {d.rain_sum > 0 ? (
                        <p>RAIN SUM: <span className="text-[9px] text-atari-cyan">{roundToOneDecimal(d.rain_sum)} mm</span></p>
                    ) : null}
                    {d.snowfall_sum > 0 ? (
                        <p>SNOW SUM: <span className="text-[9px] text-atari-cyan">{roundToOneDecimal(d.snowfall_sum)} mm</span></p>
                    ) : null}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

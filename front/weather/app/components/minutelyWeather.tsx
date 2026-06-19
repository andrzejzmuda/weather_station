"use client";

import Image from "next/image";
import { useRef, useState, useEffect } from "react";
import fetchWeather from "./queries/fetchWeather";
import { extractTime, roundToOneDecimal } from "./utils/dataFormatter";
import { getWeatherIconByCode, getWeatherAnimation } from "./utils/weatherIconByCode";


export default function MinutelyWeather({ geo_id }: { geo_id: number }) {

  const [minutelyList, setMinutelyList] = useState([]);
  const url = "minutely15weather/"
  const intervalMinute = 300000 ; // 5 minutes
  const scrollRef = useRef<HTMLDivElement>(null);
  const [isDown, setIsDown] = useState(false);
  const [startX, setStartX] = useState(0);
  const [scrollLeft, setScrollLeft] = useState(0);

  const minutely = () => {
    return fetchWeather({ url, geo_id });
  };

  useEffect(() => {
    if (!geo_id) return;

    async function load() {
      const data = await minutely();
      setMinutelyList(data);
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
        {minutelyList.map((item) => {
        const icon = getWeatherIconByCode(item.weather_code);
        const anim = getWeatherAnimation(item.weather_code);

        return (
          <div
            key={item.id}
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
                {extractTime(item.date)}
              </p>
            </div>

            <div className="font-pixel text-[10px] space-y-1 leading-tight">
              <p>TEMP: <span className="text-[9px] text-atari-cyan">
                {roundToOneDecimal(item.temperature_2m)}°C
                </span></p>
              <p>HUMID: <span className="text-[9px] text-atari-yellow">
                {roundToOneDecimal(item.relative_humidity_2m)}%
                </span></p>

              {item.rain > 0 && (
                <p>RAIN: <span className="text-[9px] text-atari-cyan">
                  {roundToOneDecimal(item.rain)} mm
                </span></p>
              )}

              {item.snowfall > 0 && (
                <p>SNOW: <span className="text-[9px] text-atari-cyan">
                  {roundToOneDecimal(item.snowfall)} mm
                </span></p>
              )}
            </div>
          </div>
          );
    })}
        </div>
      </div>
    </div>
  );
}

"use client";

import Image from "next/image";
import { useRef, useState } from "react";
import { extractTime, roundToOneDecimal } from "./dataFormatter";
import { getWeatherIconByCode, getWeatherAnimation } from "./utils/weatherIconByCode";

export default function MinutelyWeather({ minutely }: { minutely: any[] }) {
  const scrollRef = useRef<HTMLDivElement>(null);
  const [isDown, setIsDown] = useState(false);
  const [startX, setStartX] = useState(0);
  const [scrollLeft, setScrollLeft] = useState(0);

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

  return (
    <div className="w-full flex justify-center mt-6">
      <div
        className="pixel-panel w-full max-w-3xl p-3 overflow-hidden select-none cursor-grab active:cursor-grabbing"
        ref={scrollRef}
        onMouseDown={handleMouseDown}
        onMouseLeave={handleMouseLeave}
        onMouseUp={handleMouseUp}
        onMouseMove={handleMouseMove}
      >
        <div className="inline-flex gap-3 w-max pr-3">
          {minutely.map((m, index) => {
            const icon = getWeatherIconByCode(m.weather_code);
            const anim = getWeatherAnimation(m.weather_code);

            return (
              <div
                key={index}
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
                    {extractTime(m.date)}
                  </p>
                </div>

                <div className="font-pixel text-[10px] space-y-1 leading-tight">
                  <p>TEMP: <span className="text-[9px] text-atari-cyan">{roundToOneDecimal(m.temperature_2m)}°C</span></p>
                  <p>HUMID: <span className="text-[9px] text-atari-yellow">{m.relative_humidity_2m}%</span></p>
                  <p>RAIN: <span className="text-[9px] text-atari-cyan">{roundToOneDecimal(m.rain)} mm</span></p>
                  <p>SNOW: <span className="text-[9px] text-atari-cyan">{roundToOneDecimal(m.snowfall)} mm</span></p>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

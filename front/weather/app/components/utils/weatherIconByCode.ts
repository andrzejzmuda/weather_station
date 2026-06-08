const WEATHER_MAP: Record<string,  { icon: string; anim?: string }> = {
  "0": { icon: "/icons/pixel-sun.svg", anim: "icon-blink" },

  "1,2,3": { icon: "/icons/pixel-cloud.svg" },

  "45,48": { icon: "/icons/pixel-fog.svg" },

  "51,53,55": { icon: "/icons/pixel-drizzle.svg" },

  "56,57": { icon: "/icons/pixel-freezing-drizzle.svg" },

  "61,63,65": { icon: "/icons/pixel-rain.svg", anim: "icon-rain" },

  "66,67": { icon: "/icons/pixel-freezing-rain.svg", anim: "icon-rain" },

  "71,73,75": { icon: "/icons/pixel-snow.svg", anim: "icon-snow" },

  "77": { icon: "/icons/pixel-snow-grains.svg", anim: "icon-snow" },

  "80,81,82": { icon: "/icons/pixel-rain-showers.svg", anim: "icon-rain" },

  "85,86": { icon: "/icons/pixel-snow-showers.svg", anim: "icon-snow" },

  "95": { icon: "/icons/pixel-thunder.svg", anim: "icon-shake" },

  "96,99": { icon: "/icons/pixel-thunder-hail.svg", anim: "icon-shake" },
};


export function getWeatherIconByCode(code: number): string {
  for (const key of Object.keys(WEATHER_MAP)) {
    const codes = key.split(",").map(Number);
    if (codes.includes(code)) {
      return WEATHER_MAP[key].icon;
    }
  }
  return "/icons/pixel-cloud.svg"; // fallback
}


export function getWeatherAnimation(code: number): string {
  for (const key of Object.keys(WEATHER_MAP)) {
    const codes = key.split(",").map(Number);
    if (codes.includes(code)) {
      return WEATHER_MAP[key].anim ?? "";
    }
  }
  return "";
}

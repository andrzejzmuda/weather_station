import CurrentWeatherList from "../components/currentWeatherList";

export default async function CityWeatherPage({ params,}: {
  params: Promise<{ geo_id: string }>;
  }) {
    const { geo_id } = await params;

  return <CurrentWeatherList geo_id={Number(geo_id)} />;
}



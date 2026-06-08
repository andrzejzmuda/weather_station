export default async function fetchWeather({
        url,
        geo_id,
    }: {
        url: string;
        geo_id?: number;
    }) {
    const apiUrl = `${process.env.NEXT_PUBLIC_API_URL}`;
    const token = process.env.NEXT_PUBLIC_API_TOKEN;

    const fullUrl = geo_id
        ? `${apiUrl}${url}?geo_id=${geo_id}`
        : `${apiUrl}${url}`;

    try {
        const response = await fetch(fullUrl, {
            headers: {
                'Authorization': `Token ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            const text = await response.text();
            console.error("❌ FETCH ERROR");
            console.error("URL:", fullUrl);
            console.error("STATUS:", response.status, response.statusText);
            console.error("BODY:", text);
            throw new Error(`API error: ${response.status}`);
        }

        const data = await response.json();

        return data.results ?? data;

    } catch (error) {
        console.error('Error fetching weather data:', error);
        throw error;
    }
}
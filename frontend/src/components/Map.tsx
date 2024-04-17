import Mapbox from 'react-map-gl';
import "mapbox-gl/dist/mapbox-gl.css";

export const Map = () => {
  const handleClick = async (e: mapboxgl.MapLayerMouseEvent) => {
    try {
      const response = await fetch(import.meta.env.VITE_SERVER_URL, {
        method: "POST",
        body: JSON.stringify(e.lngLat)
      })
      alert(`Max wave height at ${e.lngLat.lng}, ${e.lngLat.lat} during 2019-01-01 was ${await response.text()}`)
    } catch (error) {
      alert(`Failed fetchin max wave height: ${error}`)
      console.log(error)
    }
  }

  return (
    <Mapbox
      mapboxAccessToken={import.meta.env.VITE_MAPBOX_TOKEN}
      initialViewState={{ zoom: 1 }}
      style={{width: '100vw', height: '90vh'}}
      mapStyle="mapbox://styles/mapbox/streets-v9"
      onClick={handleClick}
      attributionControl={false}
      children={null}
    />
  );
}


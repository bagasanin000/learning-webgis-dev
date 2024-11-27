var map = L.map("map").setView([0, 0], 2);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
}).addTo(map);

fetch("http://localhost:5000/api/locations")
  .then((response) => response.json())
  .then((data) => {
    data.forEach((location) => {
      const geom = JSON.parse(location.geom);
      L.marker([geom.coordinates[1], geom.coordinates[0]])
        .addTo(map)
        .bindPopup(`<b>${location.name}</b><br>${location.description}`);
    });
  });

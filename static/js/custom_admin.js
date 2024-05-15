// custom_admin.js

document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('map');
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var latlngs = [];
    var polyline = L.polyline(latlngs, {color: 'red'}).addTo(map);

    map.on('click', function(e) {
        latlngs.push(e.latlng);
        polyline.setLatLngs(latlngs);
    });
});

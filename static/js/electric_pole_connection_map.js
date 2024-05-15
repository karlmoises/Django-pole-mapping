document.addEventListener("DOMContentLoaded", function () {
    if (document.getElementById("map") && document.getElementById("changelist-form")) {
        var map = L.map('map').setView([11.585, 124.4849], 11.5);
        var dark = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
            subdomains: 'abcd',
            maxZoom: 19
        });
        dark.addTo(map);

        var connections = [];
        var poles = [];

        // Fetch ElectricPoles data
        fetch('/admin/get-poles-data/')
            .then(response => response.json())
            .then(data => {
                poles = data;
                renderPoles();
            });

        function renderPoles() {
            poles.forEach(function (pole) {
                L.marker([pole.location.y, pole.location.x]).addTo(map)
                    .bindPopup(pole.name);
            });
        }

        // Function to draw lines between ElectricPoles
        function drawLines() {
            connections.forEach(function (connection) {
                var poleFrom = poles.find(pole => pole.id === connection.pole_from_id);
                var poleTo = poles.find(pole => pole.id === connection.pole_to_id);
                if (poleFrom && poleTo) {
                    var latlngs = [
                        [poleFrom.location.y, poleFrom.location.x],
                        [poleTo.location.y, poleTo.location.x]
                    ];
                    L.polyline(latlngs, { color: 'red' }).addTo(map);
                }
            });
        }

        // Fetch ElectricPoleConnection data
        fetch('/admin/get-connections-data/')
            .then(response => response.json())
            .then(data => {
                connections = data;
                drawLines();
            });
    }
});

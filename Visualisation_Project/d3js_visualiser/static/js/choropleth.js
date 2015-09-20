var width = 1280;
var height = 720;

var vis = d3.select("body").append("svg")
    .attr("width", width).attr("height", height)



d3.json("static/geojson/TX.geojson", function(json) {
    // create a first guess for the projection
    var center = d3.geo.centroid(json)
    var scale = 150;
    var offset = [width / 2, height / 2];
    var projection = d3.geo.mercator().scale(scale).center(center)
        .translate(offset);

    // create the path
    var path = d3.geo.path().projection(projection);

    // using the path determine the bounds of the current map and use
    // these to determine better values for the scale and translation
    var bounds = path.bounds(json);
    var hscale = scale * width / (bounds[1][0] - bounds[0][0]);
    var vscale = scale * height / (bounds[1][1] - bounds[0][1]);
    var scale = (hscale < vscale) ? hscale : vscale;
    var offset = [width - (bounds[0][0] + bounds[1][0]) / 2,
        height - (bounds[0][1] + bounds[1][1]) / 2
    ];

    // new projection
    projection = d3.geo.mercator().center(center)
        .scale(scale).translate(offset);
    path = path.projection(projection);

    // add a rectangle to see the bound of the svg
    vis.append("rect").attr('width', width).attr('height', height)
        .style('stroke', 'black').style('fill', 'none');

    vis.selectAll("path").data(json.features).enter().append("path")
        .attr("d", path)
        .attr('id', function(d) {
            return d.properties.PUMA;
        })
        .attr('class', 'PUMA');
});

$.ajax({
    type: "GET",
    url: 'choropleth',
    data: controller,
    success: function(json) {
        console.log(json);
        var scale = d3.scale.linear()
            .domain([d3.min(d3.values(json)), d3.max(d3.values(json))])
            .range(['red', 'green']);
        vis.selectAll('path').style('fill', function(d){
            console.log(d.properties.PUMA, d.properties.PUMA in json, scale(json[d.properties.PUMA]));
            return scale(json[d.properties.PUMA]);
        });
        // console.log(json);

    },
    error: function(request, err, ex) {}
});

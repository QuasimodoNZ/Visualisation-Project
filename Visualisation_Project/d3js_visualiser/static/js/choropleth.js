function Choropleth(){
    var zoom = d3.behavior.zoom()
        .scaleExtent([1, 100])
        .on("zoom", zoomed);

    var drag = d3.behavior.drag()
        .origin(function(d) { return d; })
        .on("dragstart", dragstarted)
        .on("drag", dragged)
        .on("dragend", dragended);

    $('svg').remove();
    var vis = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height)
        .call(zoom).on("dblclick.zoom", null);

    var g = vis.append('g');

    function refreshDataStyling(){
        $.ajax({
            type: "GET",
            url: controller.visualisation,
            data: controller,
            success: function(json) {
                console.log('json for styling: ', json);
                var scale = d3.scale.linear()
                    .domain([d3.min(d3.values(json)), d3.max(d3.values(json))])
                    .range(['red', 'green']);
                vis.selectAll('path').style('fill', function(d){
                    if (controller.visualisation == 'choropleth-country'){
                        return scale(json[d.properties.STATE]);
                    } else if (controller.visualisation == 'choropleth-state'){
                        return scale(json[d.properties.PUMA]);
                    } else {
                        throw error ('Trying to draw a choropleth with visualisation: ' + controller.visualisation);
                    }
                });
            },
            error: function(request, err, ex) {}
        });
    }

    // var map = "";
    function refreshMap(){
        console.log('refreshing map: ', "static/geojson/" + controller.map + ".geojson");
        d3.json("static/geojson/" + controller.map + ".geojson", function(error, json) {
            if (error) throw error;
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
            // g.append("rect").attr('width', width).attr('height', height)
            //     .style('stroke', 'none').style('fill', 'none');
            g.selectAll("path").remove();
            g.selectAll("path").data(json.features).enter().append("path")
                .attr("d", path)
                // .style('stroke', 'black')
                .attr('id', function(d) {
                    if (controller.visualisation == 'choropleth-country'){
                        return d.properties.STATE
                    } else if (controller.visualisation == 'choropleth-state'){
                        return d.properties.PUMA;
                    } else {
                        throw error ('Trying to draw a choropleth with visualisation: ' + controller.visualisation);
                    }
                })
                .attr('class', controller.visualisation == 'choropleth-country' ? 'STATE' :'PUMA')
                .on('click', function(d){
                    console.log(this.id, ' was clicked');
                    selectID(this.id);
                })
                .on('dblclick', function(d){
                    if ('STATE' in d.properties){
                        controller.visualisation = 'choropleth-state';
                        controller.state = this.id;
                    } else {
                        console.log('got else');
                    }
                    visualisation.redrawFunction();
                    // console.log('clicked - d: ', d, ', i: ', i, ', this: ', this);
                });

            // When ever we redraw the map we will probable have to refresh the styling as well
            refreshDataStyling();
        });
    }

    this.redrawFunction = function(){
        evaluateQuery();
        if (controller.visualisation == 'choropleth-state' && controller.map != stateCodes[controller.state]){
            console.log('drawing state')
            console.log('controller.map: ', controller.map, ', stateCodes[controller.state]: ', stateCodes[controller.state]);
            controller.map = stateCodes[controller.state];
            refreshMap();
        } else if (controller.visualisation == 'choropleth-country' && controller.map != 'States'){
            console.log('drawing country');
            controller.map = 'States';
            refreshMap();
        } else {
            console.log('refreshing the style');
            refreshDataStyling();
        }
    };

    function zoomed() {
      g.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
    }

    function dragstarted(d) {
      d3.event.sourceEvent.stopPropagation();
      d3.select(this).classed("dragging", true);
    }

    function dragged(d) {
      d3.select(this).attr("cx", d.x = d3.event.x).attr("cy", d.y = d3.event.y);
    }

    function dragended(d) {
      d3.select(this).classed("dragging", false);
    }
}

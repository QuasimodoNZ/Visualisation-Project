function Choropleth() {
    var zoom = d3.behavior.zoom()
        .scaleExtent([1, 100])
        .on("zoom", zoomed);

    var drag = d3.behavior.drag()
        .origin(function(d) {
            return d;
        })
        .on("dragstart", dragstarted)
        .on("drag", dragged)
        .on("dragend", dragended);

    $('svg').remove();
    var vis = d3.select("#choropleth-content").append("svg")
        .attr("width", width)
        .attr("height", height)
        .on('click', function(d) {
            if (d3.event.defaultPrevented) return;
            selectID('', d3.event.shiftKey);
        })
        .call(zoom).on("dblclick.zoom", null); // removes the scrolling zoom for double clicking

    var g = vis.append('g').attr('stroke-width', '2px');

    var groupMain = g.append('g').attr('id', 'group-main');
    var groupSelected = g.append('g')
        .attr('id', 'group-selected');

    var tooltip = d3.select('#tooltip');

    function refreshDataStyling() {
        $.ajax({
            type: "GET",
            url: controller.visualisation,
            data: controller,
            success: function(json) {
                var scale = d3.scale.linear()
                    .domain([d3.min(d3.values(json)), d3.max(d3.values(json))])
                    .range(['red', 'green']);
                vis.selectAll('path').style('fill', function(d) {
                    if (controller.visualisation == 'choropleth-country') {
                        d.properties.VALUE = json[d.properties.STATE];
                    } else if (controller.visualisation == 'choropleth-state') {
                        d.properties.VALUE = json[d.properties.PUMA];
                    }
                    return scale(d.properties.VALUE);
                });
                selectedIDs.forEach(function(selectedID) {
                    console.log('reselecting id', selectedID);
                    if ($('#' + selectedID).length){
                        $('#' + selectedID).appendTo('#group-selected');
                    }
                    // } else if (pumaGroupings[controller.state] && pumaGroupings[controller.state][selectedID]){
                    //     pumaGroupings[controller.state][selectedID].forEach(function(pumaGroup){
                    //         console.log('pumaGroup: ', pumaGroup);
                    //     });
                    // }
                });
            },
            error: function(request, err, ex) {}
        });
    }

    // var map = "";
    function refreshMap() {
        d3.json("static/geojson/" + controller.map + ".geojson", function(error, json) {
            if (error) throw error;
            // create a first guess for the projection
            var width = vis.attr('width'), height = vis.attr('height');
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
            projection = d3.geo.albersUsa()//.center(center)
                .scale(scale).translate(offset);
            path = path.projection(projection);

            groupMain.selectAll("path").remove();
            groupSelected.selectAll("path").remove();

            groupMain.selectAll("path").data(json.features).enter().append("path")
                .attr("d", path)
                // .style('stroke', 'black')
                .attr('id', function(d) {
                    if (controller.visualisation == 'choropleth-country') {
                        return d.properties.STATE
                    } else if (controller.visualisation == 'choropleth-state') {
                        return d.properties.PUMA;
                    } else {
                        throw error('Trying to draw a choropleth with visualisation: ' + controller.visualisation);
                    }
                })
                .attr('class', controller.visualisation == 'choropleth-country' ? 'STATE' : 'PUMA')
                .on('click', function(d) {
                    if (d3.event.defaultPrevented) return;
                    selectID(this.id, d3.event.shiftKey);
                    d3.event.stopPropagation();
                })
                .on('dblclick', function(d) {
                    if ('STATE' in d.properties) {
                        controller.visualisation = 'choropleth-state';
                        controller.state = this.id;
                        selectedIDs = [];
                    }
                    visualisation.redrawFunction();
                }).on("mousemove", function(d) {
                    if (!$(this).is(':last-child')) {
                        $(this).appendTo($(this).parent());
                    }
                    var mouse = d3.mouse(d3.select('body').node());

                    if (!$(tooltip).is('.hidden')) {
                        tooltip.classed('hidden', false);
                    }
                    if ('STATE' in d.properties) {
                        tooltip.attr('style', 'left:' + (mouse[0] + 15) +
                                'px; top:' + (mouse[1] - 35) + 'px')
                            .html(d.properties.NAME + ': ' + (d.properties.VALUE || 'NA'));
                    } else {
                        tooltip.attr('style', 'left:' + (mouse[0] + 15) +
                                'px; top:' + (mouse[1] - 35) + 'px')
                            .html(d.properties.PUMA + ': ' + (d.properties.VALUE || 'NA'));
                    }
                })
                .on("mouseout", function() {
                    tooltip.classed('hidden', true);
                });

            // When ever we redraw the map we will probable have to refresh the styling as well
            refreshDataStyling();
        });
    }

    this.redrawFunction = function() {
        evaluateQuery();
        if (controller.visualisation == 'choropleth-country' && controller.map != 'States') {
            controller.map = 'States';
            refreshMap();
            selectedID = '';
        } else if (controller.visualisation == 'choropleth-state' && controller.map != stateCodes[controller.state][0]) {
            controller.map = stateCodes[controller.state][0];
            refreshMap();
            selectedID = '';
        } else {
            refreshDataStyling();
        }
    };

    function zoomed() {
        g.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
        g.style("stroke-width", 1.5 / d3.event.scale + "px");
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

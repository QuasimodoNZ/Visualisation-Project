function Bar() {
    $('svg').remove();

    var margin = {
            top: 20,
            right: 20,
            bottom: 150,
            left: 80
        },
        barWidth = width - margin.left - margin.right,
        barHeight = height - margin.top - margin.bottom;

    var x = d3.scale.ordinal()
        .rangeRoundBands([0, barWidth], .1);

    var y = d3.scale.linear()
        .rangeRound([barHeight, 0]);

    var color = d3.scale.category20b();
        // .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .tickFormat(d3.format(".2s"));

    var svg = d3.select("#bar-content").append("svg")
        .attr("width", barWidth + margin.left + margin.right)
        .attr("height", barHeight + margin.top + margin.bottom)
        .on('click', function(d) {
            if (d3.event.defaultPrevented) return;
            selectID('', d3.event.shiftKey);
        })
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var groupMain = svg.append('g').attr('id', 'group-main');
    var groupSelected = svg.append('g')
        .attr('id', 'group-selected').attr('stroke-width', '2px');

    svg.append("g")
        .attr("class", "y axis")

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + barHeight + ")")

    var tooltip = d3.select('#tooltip');

    this.redrawFunction = function() {
        evaluateQuery();
        $.ajax({
            type: "GET",
            url: controller.visualisation,
            data: controller,
            success: function(json) {
                $('#group-selected').children().appendTo('#group-main');

                var metricGroups = [];
                json[0].metrics.forEach(function(d) {
                    metricGroups.push(d[0]);
                });

                color.domain(metricGroups);

                json.forEach(function(d) {
                    var y0 = 0;
                    d.values = color.domain().map(function(name, index) {
                        return {
                            name: name,
                            y0: y0,
                            y1: y0 += +d.metrics[index][1]
                        };
                    });
                    d.total = d.values[d.values.length - 1].y1;
                });

                json.sort(function(a, b) {
                    return b.total - a.total;
                });

                x.domain(json.map(function(d) {
                    if (controller.visualisation == 'bar-state') {
                        return d.id;
                    } else {
                        return stateCodes[d.id][1];
                    }
                }));
                y.domain([0, d3.max(json, function(d) {
                    return d.total;
                })]);

                svg.selectAll('g.x.axis')
                    .transition().duration(1000)
                    .call(xAxis);

                svg.selectAll('g.x.axis')
                    .selectAll("text")
                    .style("text-anchor", "end")
                    .attr("dx", "-.8em")
                    .attr("dy", ".15em")
                    .attr("transform", function(d) {
                        return "rotate(-65)"
                    });

                svg.selectAll('g.y.axis')
                    .call(yAxis);

                var states = groupMain.selectAll(".STATE")
                    .data(json, function(d) {
                        return d.id;
                    })

                states.exit().remove();

                states.enter().append("g")
                    .attr("class", "STATE")
                    .attr('id', function(d) {
                        return d.id;
                    });

                states.attr("transform", function(d) {
                        var label;
                        if (controller.visualisation == 'bar-state') {
                            label = d.id;
                        } else {
                            label = stateCodes[d.id][1];
                        }
                        return "translate(" + x(label) + ",0)";
                    })
                    .on('click', function(d) {
                        if (d3.event.defaultPrevented) return;
                        selectID(this.id, d3.event.shiftKey);
                        d3.event.stopPropagation();
                    })
                    .on('dblclick', function(d) {
                        if (controller.visualisation = 'bar-country') {
                            controller.visualisation = 'bar-state';
                            controller.state = this.id;
                            selectedIDs = [];
                        }
                        visualisation.redrawFunction()
                    })
                    .on("mousemove", function(d) {
                        if (!$(this).is(':last-child')) {
                            $(this).appendTo($(this).parent());
                        }
                        var mouse = d3.mouse(d3.select('body').node());

                        if (!$(tooltip).is('.hidden')) {
                            tooltip.classed('hidden', false);
                        }
                        var label;
                        if (controller.visualisation == 'bar-state') {
                            label = d.id;
                        } else {
                            label = stateCodes[d.id][1];
                        }
                        tooltip.attr('style', 'left:' + (mouse[0] + 15) +
                                'px; top:' + (mouse[1] - 35) + 'px')
                            .html(label + ': ' + d.total);

                    })
                    .on("mouseout", function() {
                        tooltip.classed('hidden', true);
                    });

                var layers = states.selectAll("rect")
                    .data(function(d) {
                        return d.values;
                    }, function(val) {
                        return val.name;
                    });

                layers.exit().remove();

                layers.enter().append("rect");

                layers.attr("width", x.rangeBand())
                    .attr("y", function(d) {
                        return y(d.y1);
                    })
                    .attr("height", function(d) {
                        return y(d.y0) - y(d.y1);
                    })
                    .style("fill", function(d) {
                        return color(d.name);
                    });

                var legend = svg.selectAll(".legend")
                    .data(color.domain().slice().reverse(), function(d) {
                        return d;
                    })


                legend.enter().append("g")
                    .attr("class", "legend")

                legend.transition().attr("transform", function(d, i) {
                    return "translate(0," + i * 20 + ")";
                });

                legend.append("rect").transition()
                    .attr("x", barWidth - 18)
                    .attr("width", 18)
                    .attr("height", 18)
                    .style("fill", color);

                legend.append("text").transition()
                    .attr("x", barWidth - 24)
                    .attr("y", 9)
                    .attr("dy", ".35em")
                    .style("text-anchor", "end")
                    .text(function(d) {
                        return d == 'id' || d == 'POP' ? 'Population' : choices[d].verbose_name;
                    });
                legend.exit().transition().remove();


                clearNonExistentSelection();
                selectedIDs.forEach(function(selectedID) {
                    $('#' + selectedID).appendTo('#group-selected');
                });

            }
        });
    };
}

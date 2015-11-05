function Bar() {
    // var n = 4, // number of layers
    // m = 58, // number of samples per layer
    // stack = d3.layout.stack(),
    // layers = stack(d3.range(n).map(function() { return bumpLayer(m, .1); })),
    // yGroupMax = d3.max(layers, function(layer) { return d3.max(layer, function(d) { return d.y; }); }),
    // yStackMax = d3.max(layers, function(layer) { return d3.max(layer, function(d) { return d.y0 + d.y; }); });
    //
    // var margin = {top: 40, right: 10, bottom: 20, left: 10},
    //     width = 960 - margin.left - margin.right,
    //     height = 500 - margin.top - margin.bottom;
    //
    // var x = d3.scale.ordinal()
    //     .domain(d3.range(m))
    //     .rangeRoundBands([0, width], .08);
    //
    // var y = d3.scale.linear()
    //     .domain([0, yStackMax])
    //     .range([height, 0]);
    //
    // var color = d3.scale.linear()
    //     .domain([0, n - 1])
    //     .range(["#aad", "#556"]);
    //
    // var xAxis = d3.svg.axis()
    //     .scale(x)
    //     .tickSize(0)
    //     .tickPadding(6)
    //     .orient("bottom");
    //
    // $('svg').remove();
    // var svg = d3.select("#bar-content").append("svg")
    //     .attr("width", width + margin.left + margin.right)
    //     .attr("height", height + margin.top + margin.bottom)
    //   .append("g")
    //     .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    //
    // var layer = svg.selectAll(".layer")
    //     .data(layers)
    //   .enter().append("g")
    //     .attr("class", "layer")
    //     .style("fill", function(d, i) { return color(i); });
    //
    // var rect = layer.selectAll("rect")
    //     .data(function(d) { return d; })
    //   .enter().append("rect")
    //     .attr("x", function(d) { return x(d.x); })
    //     .attr("y", height)
    //     .attr("width", x.rangeBand())
    //     .attr("height", 0);
    //
    // rect.transition()
    //     .delay(function(d, i) { return i * 10; })
    //     .attr("y", function(d) { return y(d.y0 + d.y); })
    //     .attr("height", function(d) { return y(d.y0) - y(d.y0 + d.y); });
    //
    // svg.append("g")
    //     .attr("class", "x axis")
    //     .attr("transform", "translate(0," + height + ")")
    //     .call(xAxis);
    //
    // d3.selectAll("input").on("change", change);
    //
    // var timeout = setTimeout(function() {
    //   d3.select("input[value=\"grouped\"]").property("checked", true).each(change);
    // }, 2000);
    //
    // function change() {
    //   clearTimeout(timeout);
    //   if (this.value === "grouped") transitionGrouped();
    //   else transitionStacked();
    // }
    //
    // function transitionGrouped() {
    //   y.domain([0, yGroupMax]);
    //
    //   rect.transition()
    //       .duration(500)
    //       .delay(function(d, i) { return i * 10; })
    //       .attr("x", function(d, i, j) { return x(d.x) + x.rangeBand() / n * j; })
    //       .attr("width", x.rangeBand() / n)
    //     .transition()
    //       .attr("y", function(d) { return y(d.y); })
    //       .attr("height", function(d) { return height - y(d.y); });
    // }
    //
    // function transitionStacked() {
    //   y.domain([0, yStackMax]);
    //
    //   rect.transition()
    //       .duration(500)
    //       .delay(function(d, i) { return i * 10; })
    //       .attr("y", function(d) { return y(d.y0 + d.y); })
    //       .attr("height", function(d) { return y(d.y0) - y(d.y0 + d.y); })
    //     .transition()
    //       .attr("x", function(d) { return x(d.x); })
    //       .attr("width", x.rangeBand());
    // }
    //
    // // Inspired by Lee Byron's test data generator.
    // function bumpLayer(n, o) {
    //
    //   function bump(a) {
    //     var x = 1 / (.1 + Math.random()),
    //         y = 2 * Math.random() - .5,
    //         z = 10 / (.1 + Math.random());
    //     for (var i = 0; i < n; i++) {
    //       var w = (i / n - y) * z;
    //       a[i] += x * Math.exp(-w * w);
    //     }
    //   }
    //
    //   var a = [], i;
    //   for (i = 0; i < n; ++i) a[i] = o + o * Math.random();
    //   for (i = 0; i < 5; ++i) bump(a);
    //   return a.map(function(d, i) { return {x: i, y: Math.max(0, d)}; });
    // }

    var margin = {
            top: 20,
            right: 20,
            bottom: 30,
            left: 40
        },
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    var x = d3.scale.ordinal()
        .rangeRoundBands([0, width], .1);

    var y = d3.scale.linear()
        .rangeRound([height, 0]);

    var color = d3.scale.ordinal()
        .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .tickFormat(d3.format(".2s"));

    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


    this.redrawFunction = function() {
        evaluateQuery();
        console.log('controller: ', controller);
        $.ajax({
            type: "GET",
            url: controller.visualisation,
            data: controller,
            success: function(json) {
                console.log('json: ', json);

                var metricGroups = [];
                json[0].metrics.forEach(function(d){
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

                console.log('json: ', json);

                json.sort(function(a, b) {
                    return b.total - a.total;
                });

                x.domain(json.map(function(d) {
                    return stateCodes[d.id];
                }));
                y.domain([0, d3.max(json, function(d) {
                    return d.total;
                })]);

                svg.append("g")
                    .attr("class", "x axis")
                    .attr("transform", "translate(0," + height + ")")
                    .call(xAxis);

                svg.append("g")
                    .attr("class", "y axis")
                    .call(yAxis)
                    .append("text")
                    .attr("transform", "rotate(-90)")
                    .attr("y", 6)
                    .attr("dy", ".71em")
                    .style("text-anchor", "end")
                    .text("Population");

                svg.selectAll(".state")
                    .data(json)
                    .exit().remove();

                var state = svg.selectAll(".state")
                    .data(json)
                    .enter().append("g")
                    .attr("class", "g")
                    .attr("transform", function(d) {
                        return "translate(" + x(stateCodes[d.id]) + ",0)";
                    });

                state.selectAll("rect")
                    .data(function(d) {
                        return d.values;
                    })
                    .enter().append("rect")
                    .attr("width", x.rangeBand())
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
                    .data(color.domain().slice().reverse())
                    .enter().append("g")
                    .attr("class", "legend")
                    .attr("transform", function(d, i) {
                        return "translate(0," + i * 20 + ")";
                    });

                legend.append("rect")
                    .attr("x", width - 18)
                    .attr("width", 18)
                    .attr("height", 18)
                    .style("fill", color);

                legend.append("text")
                    .attr("x", width - 24)
                    .attr("y", 9)
                    .attr("dy", ".35em")
                    .style("text-anchor", "end")
                    .text(function(d) {
                        return choices[d].verbose_name;
                    });
            }
        });
    };
}

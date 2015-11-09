function Chord() {
    $('svg').remove();

    var innerRadius = Math.min(width, height) * .36,
        outerRadius = innerRadius * 1.1;
    console.log(width, height);

    var fill = d3.scale.category20c()
        .domain(d3.range(20));
        // .range(["#000000", "#FFDD89", "#957244", "#F26223"]);

    var svg = d3.select("#chord-content").append("svg")
        .attr("width", width)
        .attr("height", height)
        .on('click', function(d) {
            if (d3.event.defaultPrevented) return;
            selectID('', d3.event.shiftKey);
        })
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    var groupMain = svg.append('g').attr('id', 'group-main');
    var groupSelected = svg.append('g')
        .attr('id', 'group-selected');


    // Returns an array of tick angles and labels, given a group.
    function groupTicks(d) {
        var k = (d.endAngle - d.startAngle) / d.value;
        return d3.range(0, d.value, 1000).map(function(v, i) {
            return {
                angle: v * k + d.startAngle,
                label: i % 5 ? null : v / 1000 + "k"
            };
        });
    }

    // Returns an event handler for fading a given chord group.
    function fade(opacity) {
        return function(g, i) {
            svg.selectAll(".chord path")
                .filter(function(d) {
                    return d.source.index != i && d.target.index != i;
                })
                .transition()
                .style("opacity", opacity);
        };
    }

    this.redrawFunction = function() {
        evaluateQuery();
        $.ajax({
            type: "GET",
            url: controller.visualisation,
            data: controller,
            success: function(json) {
                console.log('chord json: ', json);
                var indexCodes = json.indicies;
                var chord = d3.layout.chord()
                    .padding(.05)
                    .sortSubgroups(d3.descending)
                    .matrix(json.matrix);

                groupMain.selectAll("path")
                    .data(chord.groups)
                    .enter().append("path")
                    .style("fill", function(d) {
                        return fill(d.index);
                    })
                    .attr('id', function(d){return indexCodes[d.index];})
                    .attr("d", d3.svg.arc().innerRadius(innerRadius).outerRadius(outerRadius))
                    .on('click', function(d) {
                        if (d3.event.defaultPrevented) return;
                        selectID(this.id, d3.event.shiftKey);
                        d3.event.stopPropagation();
                    })
                    .on("mouseover", fade(.1))
                    .on("mouseout", fade(1));

                // not sure of this
                svg.append("g").selectAll("path")
                    .data(chord.groups)
                    .enter().append("svg:text")
                    .each(function(d) { d.angle = (d.startAngle + d.endAngle) / 2; })
                    .attr("dy", ".35em")
                    .attr("text-anchor", function(d) { return d.angle > Math.PI ? "end" : null; })
                    .attr("transform", function(d) {
                      return "rotate(" + (d.angle * 180 / Math.PI - 90) + ")"
                          + "translate(" + (outerRadius + 26) + ")"
                          + (d.angle > Math.PI ? "rotate(180)" : "");
                    })
                    .text(function(d) { return indexCodes[d.index]; });


                // var ticks = svg.append("g").selectAll("g")
                //     .data(chord.groups)
                //     .enter().append("g").selectAll("g")
                //     .data(groupTicks)
                //     .enter().append("g")
                //     .attr("transform", function(d) {
                //         return "rotate(" + (d.angle * 180 / Math.PI - 90) + ")" + "translate(" + outerRadius + ",0)";
                //     });
                //
                // ticks.append("line")
                //     .attr("x1", 1)
                //     .attr("y1", 0)
                //     .attr("x2", 5)
                //     .attr("y2", 0)
                //     .style("stroke", "#000");
                //
                // ticks.append("text")
                //     .attr("x", 8)
                //     .attr("dy", ".35em")
                //     .attr("transform", function(d) {
                //         return d.angle > Math.PI ? "rotate(180)translate(-16)" : null;
                //     })
                //     .style("text-anchor", function(d) {
                //         return d.angle > Math.PI ? "end" : null;
                //     })
                //     .text(function(d) {
                //         return d.label;
                //     });

                svg.append("g")
                    .attr("class", "chord")
                    .selectAll("path")
                    .data(chord.chords)
                    .enter().append("path")
                    .attr("d", d3.svg.chord().radius(innerRadius))
                    .style("fill", function(d) {
                        return fill(d.target.index);
                    })
                    .style("opacity", 1);
                }
            });
    };
}

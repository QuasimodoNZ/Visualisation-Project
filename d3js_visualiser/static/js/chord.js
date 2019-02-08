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

    var chords = svg.append("g")
        .attr("class", "chord");
    var labelsGroup = svg.append('g');


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
                console.log('indexCodes: ', indexCodes);
                var chord = d3.layout.chord()
                    .padding(.05)
                    .sortSubgroups(d3.descending)
                    .matrix(json.matrix);

                var labelGenerator = function(d) {
                    var f = function(d) {
                        if (controller.visualisation == 'chord-country'){
                            return stateCodes[indexCodes[d.index]][1];
                        } else {
                            return visualisation.state + ':' + indexCodes[d.index];
                        }
                    };
                    // console.log(d);
                    var r = f(d);
                    // console.log(r);
                    if (!r){
                        console.log('must have been undefined: ', r, d);
                    }
                    return r
                };

                var arcs = groupMain.selectAll("path")
                    .data(chord.groups, function(d){return indexCodes[d.index];});

                arcs.enter().append("path")
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
                    .on("mousemove", fade(.1))
                    .on("mouseout", fade(1))
                    .on('dblclick', function(d) {
                        if (controller.visualisation = 'country-state') {
                            controller.visualisation = 'chord-state';
                            controller.state = this.id;
                            selectedIDs = [];
                            console.log('state id', controller.state);
                        }
                        visualisation.redrawFunction();
                    });
                arcs.exit().remove();

                var labels = labelsGroup.selectAll("path")
                                    .data(chord.groups, labelGenerator)
                labels.exit().remove();

                // not sure of this
                labels.enter().append("svg:text")
                    .each(function(d) { d.angle = (d.startAngle + d.endAngle) / 2; })
                    .attr("dy", ".35em")
                    .attr("text-anchor", function(d) { return d.angle > Math.PI ? "end" : null; })
                    .attr("transform", function(d) {
                      return "rotate(" + (d.angle * 180 / Math.PI - 90) + ")"
                          + "translate(" + (outerRadius + 26) + ")"
                          + (d.angle > Math.PI ? "rotate(180)" : "");
                    })
                    .text(labelGenerator);

                var chordLabelGenerator = function(d){
                    return labelGenerator(d.source) + '-' + labelGenerator(d.target);
                }

                chords.selectAll("path")
                    .data(chord.chords, chordLabelGenerator)
                    .enter().append("path")
                    .attr("d", d3.svg.chord().radius(innerRadius))
                    .style("fill", function(d) {
                        return fill(d.target.index);
                    })
                    .style("opacity", 1);

                chords.selectAll("path")
                    .data(chord.chords, chordLabelGenerator)
                    .exit().remove();
                }
            });
    };
}

function Force(){
    // Define the dimensions of the visualization. We're using
    // a size that's convenient for displaying the graphic on
    // http://jsDataV.is

    var width = $(document).width() - 5,
        height = $(document).height() - $('#force-content').offset().top - 5;

    this.redrawFunction = function(){
        // get the data
        $.ajax({
            type: "GET",
            url: controller.visualisation,
            data: controller,
            success: function(json) {
                console.log('json data - links: ', json);
                var nodes = json.nodes, links = json.links;
                var maxValue = d3.max(links, function(l){return l.value;}), minValue = d3.min(links, function(l){return l.value;});
                var maxWeight = d3.max(nodes, function(n){return n.prestart_weight;}), minWeight = d3.min(nodes, function(n){return n.prestart_weight;});
                console.log('minValue and maxValue: ', minValue, maxValue);
                console.log('minWeight and maxWeight: ', minWeight, maxWeight);

                var colour = d3.scale.linear()
                    .domain([minValue, maxValue])
                    .range(['red', 'green']);
                var opacity = d3.scale.linear()
                    .domain([minValue, maxValue])
                    .range([0.1, 1]);
                var radius = d3.scale.linear()
                    .domain([minWeight, maxWeight])
                    .range([5, 100]);

                console.log(radius(4), radius(5), radius(6));

                // var nodes = {};
                //
                // Compute the distinct nodes from the links.
                links.forEach(function(link) {
                    link.source = nodes[link.source];
                    link.target = nodes[link.target];
                    link.value = +link.value;
                });

                nodes.forEach(function(n){
                    console.log(n);
                    n.r = radius(n.prestart_weight);
                    console.log(n);
                    console.log();
                })

                links.sort(function(a,b){return a.value - b.value;})

                console.log('nodes: ', nodes);
                console.log('links: ', links);


                var force = d3.layout.force()
                    .nodes(d3.values(nodes))
                    .links(links)
                    .size([width, height])
                    // .linkDistance(200)
                    // .linkStrength(function(l){
                    //     console.log('link: ', l);
                    //     return l.value;
                    // })
                    .charge(function(d) {return -20 * d.r;})
                    .on("tick", tick)
                    .start();

                var svg = d3.select("body").append("svg")
                    .attr("width", width)
                    .attr("height", height);

                // build the arrow.
                svg.append("svg:defs").selectAll("marker")
                    .data(["end"])      // Different link/path types can be defined here
                  .enter().append("svg:marker")    // This section adds in the arrows
                    .attr("id", String)
                    .attr("viewBox", "0 -5 10 10")
                    .attr("refX", 15)
                    .attr("refY", -1.5)
                    .attr("markerWidth", 6)
                    .attr("markerHeight", 6)
                    .attr("orient", "auto")
                  .append("svg:path")
                    .attr("d", "M0,-5L10,0L0,5");

                // add the links and the arrows
                // var path = svg.append("svg:g").selectAll("path")
                //     .data(force.links())
                //   .enter().append("svg:path")
                // //    .attr("class", function(d) { return "link " + d.type; })
                //     .attr("class", "link")
                //     .attr("marker-end", "url(#end)")
                //     .attr('stroke', function(d){
                //         // red colour, probably want to change bassed on weight
                //         return colour(d.value);
                //     })
                //     .attr('stroke-opacity', function(d){
                //         return opacity(d.value);
                //     });

                // define the nodes
                var node = svg.selectAll(".node")
                    .data(force.nodes())
                  .enter().append("g")
                    .attr("class", "node")
                    .call(force.drag);

                // add the nodes
                node.append("circle")
                    .attr("r", function(d) {return d.r;});

                // add the text
                node.append("text")
                    .attr("x", 12)
                    .attr("dy", ".35em")
                    .text(function(d) { return d.name; });

                // add the curvy lines
                function tick() {
                    // path.attr("d", function(d) {
                    //     var dx = d.target.x - d.source.x,
                    //         dy = d.target.y - d.source.y,
                    //         dr = Math.sqrt(dx * dx + dy * dy);
                    //     return "M" +
                    //         d.source.x + "," +
                    //         d.source.y + "A" +
                    //         dr + "," + dr + " 0 0,1 " +
                    //         d.target.x + "," +
                    //         d.target.y;
                    // });

                    node
                        .attr("transform", function(d) {
                        return "translate(" + d.x + "," + d.y + ")"; });
                }
            }
        });
    };
}

function loadChart(stats) {
  google.charts.load('current', {'packages':['sankey']});
  google.charts.setOnLoadCallback(function() {drawChart(stats);});
}

function drawChart(aggregate_stats) {
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'From');
  data.addColumn('string', 'To');
  data.addColumn('number', 'Weight');
            

  data.addRows(aggregate_stats);


  var colors = ['#cab2d6', '#ffff99', '#1f78b4', '#33a02c',
                '#a6cee3', '#b2df8a', '#fb9a99', '#fdbf6f'
                ];

  // Sets chart options.
  var options = {
    width: 500,
    sankey: { 
      node: { 
        nodePadding: 40,
        colors: colors
      },
      link: {
        colorMode: 'gradient',
        colors: colors
      }
    },
  };
  // Instantiates and draws our chart, passing in some options.
  var chart = new google.visualization.Sankey(document.getElementById('sankey_basic'));
  chart.clearChart();
  chart.draw(data, options);
}

loadChart(results2021);

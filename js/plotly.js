TESTER = document.getElementById('tester');
    var trace2 = {
        x: [0, 0.5, 0.9, 1,1.2, 1.35,1.6,1.7,0],
        y: [0, 0.5, 1, 1.5,1.4, 1.3,1,0.25,0],
        fill: 'tozeroy',
        mode: 'lines+markers',
        name: 'spline',
        text: ['tweak line smoothness<br>with "smoothing" in line object', 'tweak line smoothness<br>with "smoothing" in line object', 'tweak line smoothness<br>with "smoothing" in line object', 'tweak line smoothness<br>with "smoothing" in line object', 'tweak line smoothness<br>with "smoothing" in line object', 'tweak line smoothness<br>with "smoothing" in line object'],
        line: { shape: 'spline' },
        type: 'scatter'
    };
    var layout = {
        xaxis: {range: [0, 3]},
        yaxis: {range: [0, 3]},
        legend: {
            y: 0.5,
            traceorder: 'reversed',
            font: { size: 16 },
            yref: 'paper'
        }

    };
    Plotly.newPlot('tester', [trace2], layout);
    
    
    function myFunction(){
        let hstar = document.getElementById("hstar").value;
        let bstar = document.getElementById("bstar").value;
        console.log(hstar);
        var point = {
            x: [hstar],
            y: [bstar],
            name: 'point',
            mode: 'markers',
            type: 'scatter'
        };
        Plotly.react('tester', [trace2, point], layout);
    }


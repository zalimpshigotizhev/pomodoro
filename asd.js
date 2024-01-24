

const aaa = (x, y) => {
    const xArray = x;
    const yArray = y;

    const colors = ['rgba(255,99,132,1)', 'rgba(255,205,86,1)', 'rgba(75,192,192,1)', 'rgba(54,162,235,1)', 'rgba(153,102,255,1)'];

    const data = [{
        labels: xArray,
        values: yArray,
        type: "pie",
        marker: {
            colors: colors,
            showlegend: false,
            line: {
                color: 'rgba(255,255,255,0.8)',
                width: 2
            }
        }
    }];

    const layout = {height: 300, width: 450  };

    Plotly.newPlot("myPlot", data, layout);
}

aaa(['asa', 'sasa'], [1,2])
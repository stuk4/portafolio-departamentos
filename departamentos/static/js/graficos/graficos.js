
function graficoBarrasHroizontal(id, label, labels = [], values =[], colorFondo ='rgba(2,117,216,1)', colorBordes = 'rgba(2,117,216,1)'){
    var ctx = document.getElementById(id);
    var options = {
        scales: {
          xAxes: [{
            time: {
              unit: 'month'
            },
            gridLines: {
              display: true
            },
            ticks: {
              maxTicksLimit: 6
            }
          }],
          yAxes: [{
            ticks: {
              min: 0,
              max: 15000,
              maxTicksLimit: 5
            },
            gridLines: {
              display: true
            }
          }],
        },
        legend: {
          display: true
        }
      };
      var data = {
        labels: labels,
        datasets: [{
          label: label,
          backgroundColor: colorFondo,
          borderColor: colorBordes,
          data: values,
        }],
      };
    var graficoBarras = new Chart(ctx, {
        type: 'horizontalBar',
        data: data,
        options: options
    });
    return graficoBarras;
}

function graficoRadar(id, label, labels =['Running', 'Swimming', 'Eating', 'Cycling'], values =[100, 80, 30, 2],min,max, colorFondo ='rgba(2,117,216,0.5)', colorBordes = 'rgba(2,117,216,1)'){
  var ctx = document.getElementById(id);
    var options = {
          scale: {
            angleLines: {
                display: false
            },
            ticks: {
                suggestedMin: min+1,
                suggestedMax: max+2
            }
        }
      };
      var data = {
        labels: labels,
        datasets: [{
            backgroundColor: colorFondo,
            borderColor: colorBordes,
            label:label,
            data: values
        }]
    }
    var graficoRadar = new Chart(ctx, {
        type: 'radar',
        data: data,
        options: options
    });
    return graficoRadar;
};

function graficoPie(id, label, labels =[], values =[]){


  var ctx = document.getElementById(id);
    var options = Chart.defaults.pie;
      var data = {
        labels: labels,
        datasets: [{
            backgroundColor:[
              '#E74C3C',
              '#2980B9',
              '#F4D03F',
              '#27AE60'

            ],
            label:label,
            data: values
        }]
    }
    var graficoPie = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: options
    });
    return graficoPie;
};


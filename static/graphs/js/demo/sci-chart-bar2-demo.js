// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("myBarChart2");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["عمارة", "كيمياء", "اتصالات", "مدني", "حاسبات", "ميكانيكا"],
    datasets: [{
      label: "دبلوم",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [4215, 5312, 6251, 7841, 9821, 14984],
    },{
      label: "ماجيستير",
      backgroundColor: "rgba(216,117,2,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [6215, 7312, 2251, 2841, 7821, 12984],
    },{
      label: "دكتوراة",
      backgroundColor: "rgba(216,2,2,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [5215, 6312, 4251, 3841, 4821, 11984],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
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
  }
});

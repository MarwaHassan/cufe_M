// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart4");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["الشركات التي لم تستجيب", "الشركات التي استجابت"],
    datasets: [{
      data: [30, 15.58],
      backgroundColor: ['#007bff', '#dc3545'],
    }],
  },
  options: {
    onClick : function (evt, item) {
      //alert(item[0]._model.label);
      //console.log(item[0]._model.label);
      //console.log ('legend onClick', evt);
      //console.log('legd item', item);
      window.location.replace('charts-center1.html');
    }
  }
});

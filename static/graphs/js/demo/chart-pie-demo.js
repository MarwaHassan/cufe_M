// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["مركز 1", "مركز 2", "مركز 3", "مركز 4"],
    datasets: [{
      data: [12.21, 15.58, 11.25, 8.32],
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745'],
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

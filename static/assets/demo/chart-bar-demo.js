// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["Mouse窺探",
      "怪物",
      "Law School",
      "Undercover",
      "Run On奔向愛情",
      "女神降臨",
      "五月的青春",
      "前輩，那支口紅不要塗",
      "婚詞離曲",
      "所以我和黑粉結婚了",
      "黑道律師文森佐",
      "模範計程車",
      "上流戰爭",
      "我的上流世界",
      "如蝶翩翩",
      "我是遺物整理師",
      "大發不動產",
      "黑洞",
      "在我筆下的命運",
      "某一天滅亡來到我家門前"],
    datasets: [{
      label: "Revenue",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [45, 398, 50, 22, 97, 92, 72, 194, 30, 30, 123, 124, 156, 73, 64, 117, 151, 83, 6, 296],
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
          maxTicksLimit: 20
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 500,
          maxTicksLimit: 10
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});

let myChart;
let tempArray = []
let humidArray = []
let pressureArray = []

document.addEventListener('DOMContentLoaded', async function() {

    ctx = document.getElementById('myChart').getContext('2d');

    const label = ["Current Weather Chart",];

    myChart = new Chart(ctx,{
    type: 'bar',
    data: {
        labels: label,
        datasets: [
            {
                label: 'Temperature',
                backgroundColor: "rgba(22, 54, 76, 0.43)",
                data: []
            },
            {
                label: 'Humidity',
                backgroundColor: 'rgba(3, 174, 253, 0.43)',
                data: []
            },
            {
                label: 'Pressure',
                backgroundColor: "rgba(3, 174, 123, 0.43)",
                data: []
            },
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false
            }
        }
      }
    });

    await getData();

    setInterval(getData, 10000)

});
 
function updateChart(data){
    
    value = parseInt(data.value)

   const isDataShown = myChart.isDatasetVisible(value)
   console.log(isDataShown);
   if(isDataShown === false){
       console.log('data is not shown');
       myChart.show(value)
   }else if(isDataShown === true){
       console.log('data is shown');
       myChart.hide(value)
   }


}

function addTogether(array){
    let total = 0
    for (let i=0; i<array.length; i++){
        let toadd = array[i]
        total = total + toadd
    }
    return total
 }
 

function findMinMax(array) {
    if (!array || array.length === 0) {
      return { min: undefined, max: undefined };
    }
  
    let min = array[0];
    let max = array[0];
  
    for (let i = 1; i < array.length; i++) {
      if (array[i] < min) {
        min = array[i];
      } else if (array[i] > max) {
        max = array[i];
      }
    }
  
    return { min: min, max: max };
  }

function findAverage(array){
    if (!array || array.length === 0) {
        return undefined;
      }
    total = addTogether(array)
    
    return total/array.length
}


async function getData() {
    try{
        const response = await fetch('/weatherChartData');   
        if (response){
            console.log('i got the response... Loading Data')
        }
        const data = await response.json();
        
        let tempatures = data[0].tempatures.slice(-1);
        let humidity = data[0].humidity.slice(-1);
        let pressure = data[0].pressure.slice(-1);

        tempArray.push(...tempatures.map(Number));
        humidArray.push(...humidity.map(Number));
        pressureArray.push(...pressure.map(Number));
    
        let tempMinMax = findMinMax(tempArray);
        let humidMinMax = findMinMax(humidArray);
        let pressureMinMax = findMinMax(pressureArray);

        let tempAverage = findAverage(tempArray).toFixed(2);
        let humidAverage = findAverage(humidArray).toFixed(2);
        let pressureAverage = findAverage(pressureArray).toFixed(2);


        myChart.data.datasets[0].data = tempatures;
        myChart.data.datasets[1].data = humidity;
        myChart.data.datasets[2].data = pressure;
        myChart.update();
        try{
            document.getElementById('lastUpdated').textContent = `Last Updated: ${new Date().toLocaleTimeString()}`;
            document.getElementById('tempStat').textContent = `Temperature: ${tempatures}`;
            document.getElementById('humidStat').textContent = `Humidity: ${humidity}`;
            document.getElementById('pressureStat').textContent = `Pressure: ${pressure}`;
            document.getElementById('tempMinMax').textContent = `Temperature Min/Max: ${tempMinMax.min}/${tempMinMax.max}`;
            document.getElementById('humidMinMax').textContent = `Humidity Min/Max: ${humidMinMax.min}/${humidMinMax.max}`;
            document.getElementById('pressureMinMax').textContent = `Pressure Min/Max: ${pressureMinMax.min}/${pressureMinMax.max}`;
            document.getElementById('tempAverage').textContent = `Temperature Average: ${tempAverage}`;
            document.getElementById('humidAverage').textContent = `Temperature Average: ${humidAverage}`;
            document.getElementById('pressureAverage').textContent = `Temperature Average: ${pressureAverage}`;
            } catch(error){
                console.log('On Homepage, nothing to change')
        }
        
    
    } catch (error){
        console.error(`Something went wrong: ${error} `);
    }
}




document.addEventListener('DOMContentLoaded', function(){
const minYear = document.getElementById('min_year');
const maxYear = document.getElementById('max_year');
minYearOptions = minYear.getElementsByTagName("option")
maxYearOptions = maxYear.getElementsByTagName("option")

minYear.addEventListener('change', (e)=>{
    console.log(minYear.value)
    for(maxOption of maxYearOptions){
            if(minYear.value > maxOption.value){
                maxOption.disabled = 'true'
            }
    }
})

maxYear.addEventListener('change', (e)=>{
    console.log(maxYear.value)
    for(minOption of minYearOptions){
            if(maxYear.value < minOption.value){
                minOption.disabled = 'true'
            }
    }
})
})
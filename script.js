const backendUrl = '/api/number';
let currentexpression='';
const display = document.getElementById('display');

document.querySelectorAll('.buttons button').forEach(button=>{
    button.addEventListener('click',(event)=>{
      console.log(event);
      console.log(event.target);
      console.log(event.target.textContent)
      const buttontest=event.target.textContent;
      if(buttontest==='='){
        if(currentexpression==='') return;
        display.textContent="计算中ing";
        fetch(backendUrl,{
          method:'POST',
          headers:{
          'Content-Type': 'text/plain; charset=UTF-8'
        },
        body: currentexpression,
      })
      .then(response=>response.json())
      .then(data=>{
        display.textContent=data.result;
        currentexpression=data.result;
      })
      .catch(error=>{
        console.error('Error:',error);
        display.textContent='计算出错';
      });
    }
    else if(buttontest==='C'){
      currentexpression='';
      display.textContent='0';
    }
    else{
      currentexpression+=buttontest;
      display.textContent=currentexpression;
    }
  });
});


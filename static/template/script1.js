function addNewWEField(){
  //console.log("Adding New Field");
  let newNode=document.createElement('textarea');
  newNode.classList.add('form-control');
  newNode.classList.add('weField');
  newNode.classList.add('mt-2');
  newNode.setAttribute("rows",3);
  newNode.setAttribute("placeholder","Enter here");

  let weOb=document.getElementById('we');
  let weAddButtonOb=document.getElementById('weAddButton');

  weOb.insertBefore(newNode, weAddButtonOb);
}

function addNewAQField(){
  let newNode=document.createElement('textarea');
  newNode.classList.add('form-control');
  newNode.classList.add('aqField');
  newNode.classList.add('mt-2');
  newNode.setAttribute("rows",3);
  newNode.setAttribute("placeholder","Enter here");

  let aqOb=document.getElementById('aq');
  let aqAddButtonOb=document.getElementById('aqAddButton');

  aqOb.insertBefore(newNode, aqAddButtonOb);
}

function addNewCSField(){
  let newNode=document.createElement('textarea');
  newNode.classList.add('form-control');
  newNode.classList.add('csField');
  newNode.classList.add('mt-2');
  newNode.setAttribute("rows",3);
  newNode.setAttribute("placeholder","Enter here");

  let csOb=document.getElementById('cs');
  let csAddButtonOb=document.getElementById('csAddButton');

  csOb.insertBefore(newNode, csAddButtonOb);
}

function addNewSKField(){
  let newNode=document.createElement('textarea');
  newNode.classList.add('form-control');
  newNode.classList.add('skField');
  newNode.classList.add('mt-2');
  newNode.setAttribute("rows",3);
  newNode.setAttribute("placeholder","Enter here");

  let skOb=document.getElementById('sk');
  let skAddButtonOb=document.getElementById('skAddButton');

  skOb.insertBefore(newNode, skAddButtonOb);
}

function addNewPJField(){
  let newNode=document.createElement('textarea');
  newNode.classList.add('form-control');
  newNode.classList.add('pjField');
  newNode.classList.add('mt-2');
  newNode.setAttribute("rows",3);
  newNode.setAttribute("placeholder","Enter here");

  let pjOb=document.getElementById('pj');
  let pjAddButtonOb=document.getElementById('pjAddButton');

  pjOb.insertBefore(newNode, pjAddButtonOb);
}
const ws = new WebSocket(`ws://localhost:8765/`);
console.log(location.host);

ws.onopen = e => {
  console.log("A NEW Connection established!!");
  let form = document.querySelector("#ws-form");
  form.onsubmit = e => {
    e.preventDefault();
    // create a form element
    const formData = new FormData(form);
    const reqData = {};
    console.log(formData.entries());
    for (const [key, value] of formData) {
      reqData[key] = value;
      console.log(`Key is : ${key}, Value is : ${value}`);
    }
    ws.send(JSON.stringify(reqData));
  };

};
ws.onmessage = e => {
  console.log(`MESSAGE FROM WEBSOCKET`);
  console.log(e.data);
};
ws.onerror = err => {
  console.log("We encountered an error!!");
  console.log(err);
};



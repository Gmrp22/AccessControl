const url = "http://localhost:8000/QR/user/";

const form = document.getElementById('form');

form.addEventListener('submit', submit);

function submit(event) {
  event.preventDefault();
  let name = this.elements['name'].value;
  let carnet = this.elements['carnet'].value;

  (async () => {
    const rawResponse = await fetch(url, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "name": name,
        "carnet": carnet
      })
    });
    const content = await rawResponse.json();

    console.log(content);
  })();
}
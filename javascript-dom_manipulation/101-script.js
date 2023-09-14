document.addEventListener('DOMContentLoaded', function () {
  const langCode = document.querySelector('#language_code');
  const btnTranslate = document.querySelector('#btn_translate');

  btnTranslate.addEventListener('click', function () {
    const lang = langCode.value;
    fetch(`https://hellosalut.stefanbohacek.dev/hello?lang=${lang}`)
      .then(response => response.json())
      .then(data => {
        var hello = document.querySelector('#hello');
        hello.innerHTML = data.hello;
      });
  });
});

// Aggiungi la classe "has-scrollbar" alle righe con la barra di scorrimento
document.addEventListener('DOMContentLoaded', function() {
  var rows = document.querySelectorAll('.product-row');

  function checkScrollbar(row) {
    if (row.scrollWidth > row.clientWidth) {
      row.classList.add('has-scrollbar');
    } else {
      row.classList.remove('has-scrollbar');
    }
  }

  function checkAllScrollbars() {
    rows.forEach(function(row) {
      checkScrollbar(row);
    });
  }

  checkAllScrollbars();

  window.addEventListener('resize', function() {
    checkAllScrollbars();
  });
});

function menuOnClick() {
    document.getElementById("menu-bar").classList.toggle("change");
    document.getElementById("nav").classList.toggle("change");
    document.getElementById("menu-bg").classList.toggle("change-bg");
    document.getElementById("blurr").classList.toggle("change-blurr");

}

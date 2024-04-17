// dashscript.js

$(document).ready(function() {
  $('#searchInput').on('input', function() {
    const searchText = $(this).val();
    if (searchText.length >= 3) {
      // Call function to fetch instrument data from KiteConnect API
      searchInstruments(searchText);
    } else {
      $('#searchResults').empty(); // Clear previous search results
    }
  });
});

function displayResults(results) {
  const resultList = $('#searchResults');
  resultList.empty(); // Clear previous search results

  if (results.length === 0) {
    resultList.append('<p>No results found.</p>');
  } else {
    results.forEach(function(item) {
      resultList.append(`<p>${item.tradingsymbol} - ${item.instrument_type}</p>`);
    });
  }
}

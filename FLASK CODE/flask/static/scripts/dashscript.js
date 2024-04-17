
    function searchInstruments() {
      var query = document.getElementById('searchInput').value;
      $.ajax({
        url: '/search',
        type: 'POST',
        data: { query: query },
        success: function(data) {
          displaySearchResults(data);
        },
        error: function(xhr, status, error) {
          console.error('Error:', error);
        }
      });
    }

    function displaySearchResults(data) {
      var resultsDiv = document.getElementById('searchResults');
      resultsDiv.innerHTML = ''; // Clear previous results
      data.forEach(function(item) {
        var instrumentDiv = document.createElement('div');
        instrumentDiv.textContent = item.tradingsymbol + ' - ' + item.name;
        resultsDiv.appendChild(instrumentDiv);
      });
    }

    $(document).ready(function() {
      // Bind search function to a button click event
      $('#searchBtn').click(function() {
        searchInstruments();
      });
    });
    
    function searchInstruments() {
      var query = document.getElementById('searchInput').value;
      $.ajax({
        url: '/search', // Update this URL as per your server-side route
        type: 'POST',
        data: { query: query },
        success: function(data) {
          displaySearchResults(data);
        },
        error: function(xhr, status, error) {
          console.error('Error:', error);
        }
      });
    }
    
    function displaySearchResults(data) {
      var resultsDiv = document.getElementById('searchResults');
      resultsDiv.innerHTML = ''; // Clear previous results
      data.forEach(function(item) {
        var instrumentDiv = document.createElement('div');
        instrumentDiv.textContent = item.tradingsymbol + ' - ' + item.name;
        resultsDiv.appendChild(instrumentDiv);
      });
    }
    
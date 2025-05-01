document.getElementById('vote-cats').addEventListener('click', function() {
    sendVote('cats');
});

document.getElementById('vote-dogs').addEventListener('click', function() {
    sendVote('dogs');
});

function sendVote(choice) {
    fetch('/vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ vote: choice })
    })
    .then(response => response.json())
    .then(data => {
        // Update the UI with the latest results
        document.getElementById('cats-count').textContent = data.votes.cats;
        document.getElementById('dogs-count').textContent = data.votes.dogs;
    });
}

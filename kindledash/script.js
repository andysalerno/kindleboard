// Array of inspirational quotes
const quotes = [
    {
        text: "The only way to do great work is to love what you do.",
        author: "Steve Jobs"
    },
    {
        text: "Innovation distinguishes between a leader and a follower.",
        author: "Steve Jobs"
    },
    {
        text: "Life is what happens to you while you're busy making other plans.",
        author: "John Lennon"
    },
    {
        text: "The future belongs to those who believe in the beauty of their dreams.",
        author: "Eleanor Roosevelt"
    },
    {
        text: "It is during our darkest moments that we must focus to see the light.",
        author: "Aristotle"
    },
    {
        text: "The only impossible journey is the one you never begin.",
        author: "Tony Robbins"
    }
];

// Function to update date and time
function updateDateTime() {
    const now = new Date();
    const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };

    const dateTimeString = now.toLocaleDateString('en-US', options);
    document.getElementById('datetime').textContent = dateTimeString;
}

// Function to get a random quote
function getRandomQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return quotes[randomIndex];
}

// Function to update the quote
function updateQuote() {
    const quote = getRandomQuote();
    document.getElementById('quote').textContent = `"${quote.text}"`;
    document.getElementById('author').textContent = `- ${quote.author}`;
}

// Function to simulate weather data update
function updateWeather() {
    const temperatures = [68, 70, 72, 74, 76, 78, 80];
    const conditions = ["Sunny", "Partly Cloudy", "Cloudy", "Clear", "Overcast"];
    const humidities = [45, 50, 55, 60, 65, 70, 75];

    const temp = temperatures[Math.floor(Math.random() * temperatures.length)];
    const condition = conditions[Math.floor(Math.random() * conditions.length)];
    const humidity = humidities[Math.floor(Math.random() * humidities.length)];

    document.querySelector('.temperature').textContent = `${temp}°F`;
    document.querySelector('.condition').textContent = condition;
    document.querySelector('.humidity').textContent = `Humidity: ${humidity}%`;
}

// Function to update news items
function updateNews() {
    const newsItems = [
        "Technology advances continue to shape our world",
        "New discoveries in renewable energy",
        "Space exploration reaches new milestones",
        "Scientific breakthroughs in medicine announced",
        "Environmental conservation efforts show progress",
        "Educational technology transforms learning",
        "Artificial intelligence aids in research",
        "Sustainable living practices gain momentum"
    ];

    // Select 3 random news items
    const selectedNews = [];
    const usedIndices = new Set();

    while (selectedNews.length < 3 && selectedNews.length < newsItems.length) {
        const randomIndex = Math.floor(Math.random() * newsItems.length);
        if (!usedIndices.has(randomIndex)) {
            selectedNews.push(newsItems[randomIndex]);
            usedIndices.add(randomIndex);
        }
    }

    const newsList = document.querySelector('.news-list');
    newsList.innerHTML = '';

    selectedNews.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        newsList.appendChild(li);
    });
}

// Function to update schedule
function updateSchedule() {
    const activities = [
        "Morning Reading", "Afternoon Walk", "Evening Relaxation",
        "Coffee Break", "Exercise", "Meditation", "Writing",
        "Music Practice", "Gardening", "Cooking", "Study Time"
    ];

    const times = ["9:00 AM", "11:00 AM", "2:00 PM", "4:00 PM", "7:00 PM"];

    const schedule = document.querySelector('.schedule');
    schedule.innerHTML = '';

    // Create 3 random events
    const usedActivities = new Set();
    for (let i = 0; i < 3; i++) {
        let activity;
        do {
            activity = activities[Math.floor(Math.random() * activities.length)];
        } while (usedActivities.has(activity));

        usedActivities.add(activity);

        const eventDiv = document.createElement('div');
        eventDiv.className = 'event';

        const timeSpan = document.createElement('span');
        timeSpan.className = 'time';
        timeSpan.textContent = times[i] || `${9 + i * 2}:00 ${i < 2 ? 'AM' : 'PM'}`;

        const titleSpan = document.createElement('span');
        titleSpan.className = 'title';
        titleSpan.textContent = activity;

        eventDiv.appendChild(timeSpan);
        eventDiv.appendChild(titleSpan);
        schedule.appendChild(eventDiv);
    }
}

// Initialize the page
function init() {
    updateDateTime();
    updateQuote();
    updateWeather();
    updateNews();
    updateSchedule();

    // Update time every minute
    setInterval(updateDateTime, 60000);

    // Update quote every 10 minutes
    setInterval(updateQuote, 600000);

    // Update weather every 30 minutes
    setInterval(updateWeather, 1800000);

    // Update news every hour
    setInterval(updateNews, 3600000);

    // Update schedule every 2 hours
    setInterval(updateSchedule, 7200000);
}

// Handle page refresh/reload
function handleRefresh() {
    // Refresh all dynamic content
    updateDateTime();
    updateQuote();
    updateWeather();
    updateNews();
    updateSchedule();
}

// Add event listeners
document.addEventListener('DOMContentLoaded', init);
document.addEventListener('visibilitychange', function () {
    if (!document.hidden) {
        handleRefresh();
    }
});

// Handle clicks for manual refresh (useful for Kindle)
document.addEventListener('click', function (e) {
    if (e.target.classList.contains('card') || e.target.closest('.card')) {
        const card = e.target.classList.contains('card') ? e.target : e.target.closest('.card');

        // Add a subtle visual feedback
        card.style.backgroundColor = '#f0f0f0';
        setTimeout(() => {
            card.style.backgroundColor = '#ffffff';
        }, 200);

        // Update the specific card content
        if (card.classList.contains('weather-card')) {
            updateWeather();
        } else if (card.classList.contains('quote-card')) {
            updateQuote();
        } else if (card.classList.contains('news-card')) {
            updateNews();
        } else if (card.classList.contains('calendar-card')) {
            updateSchedule();
        }
    }
});

// // Prevent zooming and scrolling on Kindle
// document.addEventListener('gesturestart', function (e) {
//     e.preventDefault();
// });

// document.addEventListener('gesturechange', function (e) {
//     e.preventDefault();
// });

// document.addEventListener('gestureend', function (e) {
//     e.preventDefault();
// });

// // Disable context menu
// document.addEventListener('contextmenu', function (e) {
//     e.preventDefault();
// });

// Ensure the page fits exactly in the Kindle viewport
function adjustForKindle() {
    const body = document.body;
    const container = document.querySelector('.container');

    // Set exact dimensions for Kindle
    body.style.width = '1072px';
    body.style.height = '1448px';
    body.style.overflow = 'hidden';

    // Prevent any scrolling
    document.documentElement.style.overflow = 'hidden';

    // Adjust font sizes if content doesn't fit
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        if (card.scrollHeight > card.clientHeight) {
            const fontSize = parseFloat(window.getComputedStyle(card).fontSize);
            card.style.fontSize = `${fontSize * 0.9}px`;
        }
    });
}

// Call adjustment function after page load
window.addEventListener('load', adjustForKindle);

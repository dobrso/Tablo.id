let socket;

// Исправленный путь WebSocket
socket = new WebSocket('ws://' + window.location.host + '/ws/notifications/');

// Инициализация Toast (без Bootstrap)
let toastElement = document.getElementById('toastBody');

socket.onopen = function(e) {
    console.log('WebSocket соединение установлено');
};

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    if (data.type === 'notification') {
        showNotification(data.title, data.author);
        updatePostsList(data.title, data.author);
    }
};

socket.onerror = function(e) {
    console.error('WebSocket ошибка:', e);
};

socket.onclose = function(e) {
    console.log('WebSocket соединение закрыто');
    // Попытка переподключения через 3 секунды
    setTimeout(function() {
        console.log('Попытка переподключения...');
        socket = new WebSocket('ws://' + window.location.host + '/ws/notifications/'); // Исправлен путь
    }, 3000);
};

function showNotification(title, author) {
    const toastBody = document.getElementById('toastBody');
    toastBody.innerHTML = `
        <div class="notification-content">
            <strong>Новый пост!</strong><br>
            <strong>${escapeHtml(title)}</strong><br>
            Автор: ${escapeHtml(author)}<br>
        </div>
    `;

    // Показываем toast
    toastBody.classList.add('show');

    // Автоматически скрыть через 10 секунд
    setTimeout(() => {
        toastBody.classList.remove('show');
    }, 10000);
}

function updatePostsList(title, author) {
    // Обновляем список постов на странице, если он есть
    const postsContainer = document.querySelector('.posts-grid'); // Исправлен селектор
    if (postsContainer) {
        const newPostHtml = `
            <article class="post-card new-post" style="animation: highlight 2s;">
                <div class="post-header">
                    <div class="author-info">
                        <div class="author-avatar">
                            <div class="avatar-placeholder">👤</div>
                        </div>
                        <div class="author-details">
                            <span class="author-name">${escapeHtml(author)}</span>
                        </div>
                    </div>
                </div>
                <h2 class="post-title">
                    <a href="#">${escapeHtml(title)}</a>
                </h2>
                <div class="post-footer">
                    <div class="post-actions">
                        <a href="#" class="read-more-btn">
                            Читать далее →
                        </a>
                    </div>
                </div>
            </article>
        `;
        postsContainer.insertAdjacentHTML('afterbegin', newPostHtml);
    }
}

// Добавляем функцию экранирования HTML
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
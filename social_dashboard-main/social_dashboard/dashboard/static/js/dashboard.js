window.onload = fetchPosts;

function getCSRFToken() {
    let cookieValue = null;
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        if (cookie.trim().startsWith('csrftoken=')) {
            cookieValue = cookie.trim().substring('csrftoken='.length);
        }
    }
    return cookieValue;
}

async function fetchPosts() {
    try {
        const res = await fetch('/api/posts/');
        if (!res.ok) {
            console.error('Failed to fetch posts:', res.status);
            return;
        }

        const posts = await res.json();
        const container = document.getElementById('posts');
        container.innerHTML = '';

        posts.forEach(post => {
            container.innerHTML += `
                <div class="card mt-4 shadow-sm">
                    <div class="card-body">
                        <h5><strong>${post.user}</strong></h5>
                        <p>${post.content}</p>

                        <button onclick="likePost(${post.id})" class="btn btn-sm btn-outline-danger">
                            ❤️ Like (${post.likes})
                        </button>

                        <hr/>
                        <h6>💬 Comments:</h6>
                        <div id="comments-${post.id}">
                            ${post.comments.map(comment => `
                                <p><strong>${comment.user}:</strong> ${comment.comment}</p>
                            `).join('')}
                        </div>

                        <form onsubmit="addComment(event, ${post.id})">
                            <input type="text" class="form-control form-control-sm mt-2"
                                   id="comment-input-${post.id}" placeholder="Write a comment..." required>
                            <button class="btn btn-sm btn-primary mt-1">Post Comment</button>
                        </form>
                    </div>
                </div>
            `;
        });

    } catch (error) {
        console.error('Error loading posts:', error);
    }
}

async function createPost(event) {
    event.preventDefault();
    const content = document.getElementById('content').value;

    const res = await fetch('/api/posts/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({ content })
    });

    if (res.ok) {
        document.getElementById('content').value = '';
        fetchPosts();
    } else {
        console.error("Post creation failed.");
    }
}

async function likePost(postId) {
    const res = await fetch(`/api/posts/${postId}/like/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken()
        }
    });

    if (res.ok) {
        fetchPosts();
    } else {
        console.error("Failed to like post.");
    }
}

async function addComment(event, postId) {
    event.preventDefault();
    const input = document.getElementById(`comment-input-${postId}`);
    const content = input.value;

    const res = await fetch('/api/comments/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({
            post: postId,
            comment: content
        })
    });

    if (res.ok) {
        input.value = '';
        fetchPosts();
    } else {
        console.error("Failed to post comment.");
    }
}

css = '''
<style>
:root {
    --dm-accent: #7c8cff;
    --dm-accent-2: #a78bfa;
    --dm-bg-user: #2b2f3d;
    --dm-bg-bot: #363c4f;
    --dm-bg-card: #23273349;
}

/* Header banner */
.dm-header {
    background: linear-gradient(120deg, #5b6cff 0%, #9b6bff 100%);
    padding: 1.6rem 2rem;
    border-radius: 1rem;
    margin-bottom: 1.2rem;
    color: white;
    box-shadow: 0 4px 18px rgba(91,108,255,0.25);
}
.dm-header h1 {
    margin: 0;
    font-size: 1.6rem;
    font-weight: 700;
}
.dm-header p {
    margin: 0.3rem 0 0 0;
    opacity: 0.9;
    font-size: 0.95rem;
}

/* Chat bubbles */
.chat-message {
    padding: 1rem 1.3rem;
    border-radius: 1rem;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: flex-start;
    gap: 0.7rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.18);
    animation: dm-fade-in 0.25s ease-out;
}
@keyframes dm-fade-in {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
}
.chat-message.user {
    background: var(--dm-bg-user);
    flex-direction: row-reverse;
    border-top-right-radius: 0.2rem;
}
.chat-message.bot {
    background: var(--dm-bg-bot);
    border-top-left-radius: 0.2rem;
}
.chat-message .avatar {
    flex-shrink: 0;
}
.chat-message .avatar img {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    color: #f1f2f6;
    line-height: 1.55;
    font-size: 0.96rem;
}
.chat-message.user .message {
    text-align: right;
}

/* Sources */
.source-box {
    background: var(--dm-bg-card);
    border-left: 3px solid var(--dm-accent);
    border-radius: 0.5rem;
    padding: 0.65rem 0.9rem;
    margin-bottom: 0.5rem;
    font-size: 0.85rem;
    color: #d3d6e0;
}
.source-box .source-title {
    color: var(--dm-accent-2);
    font-weight: 600;
    margin-bottom: 0.25rem;
    font-size: 0.82rem;
}
.source-rank {
    display: inline-block;
    background: var(--dm-accent);
    color: white;
    font-size: 0.68rem;
    font-weight: 700;
    padding: 0.05rem 0.45rem;
    border-radius: 1rem;
    margin-right: 0.4rem;
    vertical-align: middle;
}
.answer-meta {
    color: #8b90a0;
    font-size: 0.78rem;
    margin: -0.4rem 0 0.7rem 3.2rem;
}

/* Sidebar document library */
.doc-card {
    background: var(--dm-bg-card);
    border-radius: 0.6rem;
    padding: 0.55rem 0.8rem;
    margin-bottom: 0.4rem;
    font-size: 0.83rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.doc-card .doc-name {
    color: #e6e8f0;
    font-weight: 600;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    max-width: 70%;
}
.doc-card .doc-meta {
    color: #9aa0ab;
    font-size: 0.75rem;
}

/* Suggested question chips */
.chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 0.8rem;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/6134/6134346.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://png.pngtree.com/png-vector/20190321/ourmid/pngtree-vector-users-icon-png-image_856952.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

source_template = '''
<div class="source-box">
    <div class="source-title"><span class="source-rank">{{RANK}}</span>{{ICON}} {{SOURCE}} — page {{PAGE}}</div>
    <div>{{SNIPPET}}</div>
</div>
'''

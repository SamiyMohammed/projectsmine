import { useEffect, useState } from 'react';

const API = '/api/todos';

export default function App() {
const [todos, setTodos] = useState([]);
const [title, setTitle] = useState('');

useEffect(() => {
fetch(API)
.then((res) => res.json())
.then(setTodos)
.catch((err) => console.error('Failed to load todos:', err));
}, []);

async function addTodo(e) {
e.preventDefault();
if (!title.trim()) return;

const res = await fetch(API, {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ title }),
});
const newTodo = await res.json();
setTodos([newTodo, ...todos]);
setTitle('');
}

async function toggleTodo(todo) {
const res = await fetch(`${API}/${todo._id}`, {
method: 'PATCH',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ done: !todo.done }),
});
const updated = await res.json();
setTodos(todos.map((t) => (t._id === updated._id ? updated : t)));
}

async function deleteTodo(id) {
await fetch(`${API}/${id}`, { method: 'DELETE' });
setTodos(todos.filter((t) => t._id !== id));
}

return (
<div style={{ maxWidth: 480, margin: '40px auto', fontFamily: 'sans-serif' }}>
<h1>My Todos</h1>

<form onSubmit={addTodo} style={{ display: 'flex', gap: 8 }}>
<input
value={title}
onChange={(e) => setTitle(e.target.value)}
placeholder="What needs doing?"
style={{ flex: 1, padding: 8 }}
/>
<button type="submit" style={{ padding: '8px 16px' }}>
Add
</button>
</form>

<ul style={{ listStyle: 'none', padding: 0, marginTop: 20 }}>
{todos.map((todo) => (
<li
key={todo._id}
style={{ display: 'flex', alignItems: 'center', gap: 8, padding: '8px 0' }}
>
<input type="checkbox" checked={todo.done} onChange={() => toggleTodo(todo)} />
<span style={{ flex: 1, textDecoration: todo.done ? 'line-through' : 'none' }}>
{todo.title}
</span>
<button onClick={() => deleteTodo(todo._id)}>Delete</button>
</li>
))}
</ul>

{todos.length === 0 && <p>No todos yet. Add one above!</p>}
</div>
);
}
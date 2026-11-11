Todo App

A full-stack todo app built with React, Node.js, Express, and MongoDB. You can add todos, check them off, and delete them, and everything is saved in a MongoDB database.

Tech stack: React and Vite on the frontend, Node.js with Express on the backend, MongoDB Atlas for the database, and Mongoose to connect them.

Setup

First, create a MongoDB Atlas cluster and copy your connection string. In the server folder, create a file named .env and add a line with MONGO_URI set to your connection string. Never commit this file.

Then run these commands. In the server folder, run npm install, then npm start. In a second terminal, go to the client folder, run npm install, then npm run dev. Open http://localhost:5173 in your browser.

Project structure

The server folder has index.js, which runs the Express API. The client folder has the React app, with App.jsx and main.jsx inside the src folder.

API routes

GET /api/todos returns all todos. POST /api/todos creates one. PATCH /api/todos/:id updates the done status. DELETE /api/todos/:id removes one.

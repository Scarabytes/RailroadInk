window.onload = ()=>{
    let socketio = io();
    socketio.send('Hello World');
    socketio.on('message', (m)=>{
        console.log(m);
    })
};

import React, {useEffect} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  useEffect(() => {
    // during production we'll use:
    // fetch('http://127.0.0.1:5000/scripts').then(response=>{

    // during development we use:
    fetch('http://127.0.0.1:5000/clouds', {
      method:'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({
        script_id:0,
        script_obj:null,
        whole_script:true,
        action_lines:true,
        characters:'gittes,evelyn,escobar'
      })
    }).then(response=>{
      return response.json()
    }).then((data)=>{
      console.log(data)
    })
    console.log('mount it!');
}, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

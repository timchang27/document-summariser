import './App.css';

import React, {useState} from 'react'
import FileUpload from './components/FileUpload';
import Summary from './components/Summary';

const App = () => {
  const [responseData, setResponseData] = useState(null);

  const handleResponseData = (data) => {
    setResponseData(data);
  };

  return (
    <React.Fragment>
      <header>
        <h1>Document Summariser</h1>
        <h4>Upload your documents below!</h4>
      </header>
      <FileUpload onSubmit={handleResponseData}/>
      <Summary responseData={responseData}/>
      
      <footer>GitHub</footer>
    </React.Fragment>
  )
}

export default App
